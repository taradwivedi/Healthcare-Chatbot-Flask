import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('model.h5')
import json
import random
intents = json.loads(open('data.json').read())
words = pickle.load(open('texts.pkl','rb'))
classes = pickle.load(open('labels.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result
'''
def chatbot_response(msg):
    # Predict the intent of the user's message
    intents = predict_class(msg, model)
    
    # If the intent is about providing services, return a list of available services
    if intents[0]['intent'] == 'services_provided':
        response = "I can help you with the following:\n"
        for i, intent in enumerate(intents):
            if intent['tag'] in ['cough', 'fever', 'headache']:
                response += f"{i + 1}. {intent['tag'].capitalize()}\n"
        return response
    
    # If the intent is related to providing information about a specific ailment, return the corresponding response
    return getResponse(intents, intents)



'''
'''
def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res
'''
def chatbot_response(msg):
    # Check if the user's input is a number indicating a specific health concern
    if msg.isdigit():
        idx = int(msg) - 1  # Convert the input to an index (subtract 1 because indices start from 0)
        if 0 <= idx < len(intents['intents']):
            intent = intents['intents'][idx]
            if 'tag' in intent and intent['tag'] in ['cough', 'fever', 'headache']:
                # If the intent corresponds to cough, fever, or headache, return the appropriate response
                return random.choice(intent['responses'])
            else:
                # If the intent doesn't match cough, fever, or headache, return a default response
                return "Sorry, I couldn't find information for that option."
        else:
            # If the index is out of range, return a default response
            return "Please select a valid option."
    else:
        # If the user's input is not a number, proceed with the standard response retrieval process
        ints = predict_class(msg, model)
        res = getResponse(ints, intents)
        return res


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run()