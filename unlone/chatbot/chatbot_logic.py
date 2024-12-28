import os
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Initialize necessary components
lemmatizer = WordNetLemmatizer()

# Load intents, words, classes, and model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load intents, words, classes, and model
with open(os.path.join(BASE_DIR, 'mentalhealth.json'), 'r') as file:
    intents = json.load(file)

words = pickle.load(open(os.path.join(BASE_DIR, 'ChatBot_Model/words.pkl'), 'rb'))
classes = pickle.load(open(os.path.join(BASE_DIR, 'ChatBot_Model/classes.pkl'), 'rb'))
model = load_model(os.path.join(BASE_DIR, 'ChatBot_Model/chatbot_model.h5'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    if not intents_list:  # Check if the list is empty
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
    
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Main function that will be used by app.py
def generate_response(message):
    intents_list = predict_class(message)
    response = get_response(intents_list, intents)
    return response

# Only print a start-up message if this script is run directly
if __name__ == "__main__":
    print("GO! ChatBot is running!")
