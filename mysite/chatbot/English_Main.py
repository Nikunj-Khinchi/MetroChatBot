import json
import os 
import random
from  .English_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from .English_Preprocessing.stemming import stemming
from  .English_Preprocessing.removalStopWords import removal_of_stop_words
from django.conf import settings

# file_path = os.path.join(settings.BASE_DIR, 'chatbot/English_model/data.json')


with open('C:\\Users\\swast\\Desktop\\sem5\\NLP\\MetroChatBot\\mysite\\chatbot\\NeuralModel\\data.json', 'r') as f:
        intents = json.load(f)
# else:
#     print(f"The file {file_path} does not exist.")

# Preprocess user input
def preprocess_input(user_input):
    words = tokenization_of_words(user_input)
    words = removal_of_stop_words(words)
    words = stemming(words)
    return words

# Function to calculate similarity between two lists of words
def get_similarity_score(input_words, pattern_words):
    if not input_words or not pattern_words:
        return 0.0  # Return 0 if either list is empty

    common_words = set(input_words) & set(pattern_words)
    # similarity = len(common_words) / max(len(input_words), len(pattern_words))
    similarity = len(common_words) / (len(input_words)+len(pattern_words)-len(common_words))

    return similarity

# Function to get a response


# def get_responsebot(user_input):
    user_input = preprocess_input(user_input)

    best_match_intent = None
    best_match_score = 0.2  # Adjust the similarity threshold as needed
    # Iterate through the intents and patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess_input(pattern)
            similarity_score = get_similarity_score(user_input, pattern_words)
            if similarity_score > best_match_score:
                best_match_score = similarity_score
                best_match_intent = intent

    if best_match_intent and best_match_score >= 0.5:  # Adjust the similarity threshold as needed
        responses = best_match_intent['responses']
        return random.choice(responses)  # Select a random response from the available responses

    return "I'm sorry, I don't understand that."

def get_responsebot(user_input):
    user_input = preprocess_input(user_input)

    similarity_scores = []  # List to store similarity scores

    # Iterate through the intents and patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess_input(pattern)
            similarity_score = get_similarity_score(user_input, pattern_words)
            similarity_scores.append((similarity_score, intent))

    # Sort the similarity scores in descending order
    similarity_scores.sort(reverse=True, key=lambda x: x[0])

     # Print the top 5 similarity scores
    
    printed_intents = set()  # Set to track printed intents
    unique_top_5_similarity = []
    for score, matched_intent in similarity_scores:
        intent_tag = matched_intent['tag']
        if intent_tag not in printed_intents:
            print(f"Score: {score}, Intent: {intent_tag}")
            printed_intents.add(intent_tag)
            unique_top_5_similarity.append((round(score, 2)  , intent_tag))
            if len(printed_intents) == 5:
                break

    best_match_intent = None
    best_match_score = 0

    print(unique_top_5_similarity)
    # Choose the best match from the sorted list
    if similarity_scores and similarity_scores[0][0] >= 0.1:  # Adjust the similarity threshold as needed
        best_match_score, best_match_intent = similarity_scores[0]
    # if unique_top_5_similarity and unique_top_5_similarity[0][0] >= 0.5:  # Adjust the similarity threshold as needed
    #     best_match_score, best_match_intent = similarity_scores[0]


    if best_match_intent:
        responses = best_match_intent['responses']
        # print(responses)
        chosen_response = random.choice(responses)  # Select a random response from the available responses
    else:
        chosen_response = "I'm sorry, I don't understand that."

    return unique_top_5_similarity, chosen_response


# response = get_responsebot("price from road")   
# print(response)

# # Interactive loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye!")
#         break
#     response = get_response(user_input)
#     print("Chatbot:", response)
