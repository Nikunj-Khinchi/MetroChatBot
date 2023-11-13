# import random
# import json

# import torch

# from .NeuralModel import NeuralNet
# from  .NeuralModel.nltk_utils import bag_of_words, tokenize

# # from NeuralModel import NeuralNet
# # from NeuralModel.nltk_utils import bag_of_words, tokenize

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# import os
# from django.conf import settings

# file_path = os.path.join(settings.BASE_DIR, 'chatbot/English_model/data.json')
# with open(file_path, 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# bot_name = "College Bud"
# print("Let's chat! (type 'quit' to exit)")
# while True:
#     # sentence = "do you use credit cards?"
#     sentence = input("You: ")
#     if sentence == "quit":
#         break

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(f"{bot_name}: I do not understand...")


import random
import json
import torch
import os
from django.conf import settings
from .NeuralModel.model import NeuralNet
from .NeuralModel.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_model():
    # file_path = os.path.join(settings.BASE_DIR, 'chatbot/English_model/data.json')
    with open('C:/Users/Lenovo/Desktop/Dek-Work/NLP/METRO_DJANGO/MetrochatBot/mysite/chatbot/NeuralModel/data.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "C:/Users/Lenovo/Desktop/Dek-Work/NLP/METRO_DJANGO/MetrochatBot/mysite/chatbot/NeuralModel/data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    return model, intents, all_words, tags

def chatbot_response(user_text):
    model, intents, all_words, tags = load_model()
    bot_name = "College Bud"

    user_text = tokenize(user_text)
    X = bag_of_words(user_text, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return f"{bot_name}: {random.choice(intent['responses'])}"
    else:
        return f"{bot_name}: I do not understand..."

# # Example usage:
# user_input = "price from vastral to nirant cross road"
# response = chatbot_response(user_input)
# print(response)