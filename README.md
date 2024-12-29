# Healthcare Chatbot Using Flask API

![image](https://github.com/user-attachments/assets/93089046-d6b0-43be-af77-9c94f2a221bd)


## Project Overview
This repository contains the implementation of a **Healthcare Chatbot** built using Flask, designed to assist users with basic healthcare-related inquiries. The chatbot provides helpful responses for common symptoms like fever, headache, stomach ache, and cough, as well as general medical advice and medication recommendations.

## Key Features
1. **Real-life Application**:
   - The chatbot provides preliminary healthcare guidance based on user inputs.
   - Assists in symptom identification and over-the-counter medication suggestions.
   - Allows users to search for hospitals by name or location.

2. **Custom JSON Intents**:
   - The chatbot's logic is powered by a well-defined JSON file containing a set of `intents`, `patterns`, and `responses` tailored to healthcare-related topics. 
   - Example:
     ```json
     {
       "tag": "fever",
       "patterns": ["I have a fever", "Fever", "My temperature is high"],
       "responses": ["Fever can indicate an infection or illness. Make sure to rest, stay hydrated..."],
       "context": [""]
     }
     ```

3. **Powered by Flask**:
   - Flask is used to handle API requests and serve the chatbot interface.
   - The lightweight nature of Flask ensures the application is fast and scalable.

4. **Scalable Design**:
   - The chatbot is structured to allow easy addition of new intents and patterns.
   - Future deployment plans include integration with hospital databases and real-time health monitoring systems.

5. **Screenshots of Results**:
   - Screenshots of the chatbot interface and how it responds:
       - Stomachache and Headache
     ![image](https://github.com/user-attachments/assets/36a3fd96-b441-42bb-8d1f-53511120e9a4)
       - High temperature and Cough
     ![image](https://github.com/user-attachments/assets/372afdc0-2325-49e5-839e-a62deb3e4b95)
       - Medication options and Solutions if Symptoms Persist
     ![image](https://github.com/user-attachments/assets/955189f1-cfe0-47ce-9f4f-ba516e05f0f5)
       - Hospitals nearby
     ![image](https://github.com/user-attachments/assets/70211178-5c80-489d-98ca-1c082c4ca57e)
       - Response to Thank You and Bye and its variations
     ![image](https://github.com/user-attachments/assets/e4a7b022-3fe2-453e-adc0-6545d24ec007)

## Technologies Used
- **Flask**: A micro web framework for creating the chatbot API and serving the interface.
- **JSON**: Used for defining chatbot intents, patterns, and responses.
- **HTML/CSS**: For designing the chatbot UI.
- **NLP (Natural Language Processing)**: Basic pattern matching using Python for understanding user input.

## Unique Aspects of the Project

### Healthcare Focus:
- Unlike general-purpose chatbots, this project is tailored for healthcare needs.
- It acts as a virtual assistant for preliminary medical advice.

### JSON-driven Logic:
- The chatbot relies on a JSON file, making it easy to update or extend its knowledge base.

### Future-ready:
- Plans for deployment on cloud platforms (e.g., AWS, Heroku).
- Integration with hospital APIs for real-time updates.

## Future Plans

### Deploying the Chatbot:
- Host the application on a cloud service like AWS or Heroku.
- Make it publicly accessible for users.

### Real-time Hospital Data:
- Integrate APIs for live hospital data (availability, location, and services).

### Advanced Features:
- Incorporate NLP libraries (e.g., NLTK, SpaCy) for better input understanding.
- Enable real-time symptom monitoring with wearable integrations.

## Limitations

### 1. **Pattern Matching**
The chatbot relies heavily on **pattern matching**, which means it can only recognize exact or very similar inputs. If a user input differs slightly from the predefined patterns, the chatbot might not respond appropriately. The bot matches patterns directly, and any variation or deviation outside of the predefined patterns may lead to a response mismatch or no response at all.

### 2. **Lemmatization and Stemming**
The chatbot has some level of understanding of variations of words due to **lemmatization** or **stemming**. This allows it to recognize different forms of a word, such as:
- "persist", "persisting", "persistent"

However, the chatbot's understanding is limited and may not always capture more complex sentence structures or word variations. For instance:
- If the root word "persist" is detected, the bot can handle variations such as "persisting" or "persistent", but it may not recognize more complex or unrelated words.
  
Thus, the bot may miss more nuanced or complex word forms and phrasing.

### 3. **Limited Understanding**
The chatbot is not an intelligent conversational agent with **deep learning**. It is based on simple **pattern matching** and thus has a **limited understanding of natural language**. It can only recognize predefined patterns and cannot handle more sophisticated or complex inputs outside of its training data. It will struggle with ambiguous questions or any queries that are not part of its training dataset.

### 4. **Contextual Limitations**
While the bot includes context in some of the intents (e.g., `search_hospital_by_params`), it does not maintain a persistent conversation state over multiple interactions. This means that:
- Once a context is changed or the conversation moves beyond the scope of the current intent, the chatbot cannot "remember" past interactions or seamlessly transition between different topics.
- It is limited to responding within the context of a single intent at a time and does not retain memory of previous exchanges, which limits its ability to hold coherent multi-turn conversations.







