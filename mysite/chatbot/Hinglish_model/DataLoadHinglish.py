import json


# Your Hinglish_Preprocessing functions
from Hinglish_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words

from Hinglish_Preprocessing.stemming import stem_word as stemming

from Hinglish_Preprocessing.removalStopWords import Hinglish_stop_words as HindiStopWords

# Load the JSON data from 'data.json'
with open('DataHinglish.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)
    
all_stemWords = []
tags = []
dataPattern = []

# Process the intents
count = 0
for intent in intents["intents"]:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        print("************* Data Processing", count, "**************\n")
        count = count+1
        print("Data", pattern, "\n")
        w = tokenization_of_words(pattern)
        print("Data After Tokenization", w, "\n")
        w1 = HindiStopWords(w)
        print("Data After Removal of Stopwords", w1, "\n")
        
        stemmed_words = []
        for word in w1:
            w2 = stemming(word)
            stemmed_words.append(w2)
        print("Data After stemming", stemmed_words , "\n")
          # create our training data
        join_words = ' '.join(stemmed_words)
        print("Final Data : ", join_words, "\n\n\n\n\n")
        dataPattern.extend((tag , stemmed_words))



print(len(dataPattern), "patterns" , dataPattern , '\n')
print(len(tags), "tags:", tags , '\n')
