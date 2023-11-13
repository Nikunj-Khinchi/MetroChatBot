content_list = []
import os
from django.conf import settings

file_path = os.path.join(settings.BASE_DIR, 'chatbot/Hinglish_Preprocessing/hinglishstopwords.txt')


with open(file_path, 'r') as file:  
    content_list = []
    for line in file.readlines():
        content_list.append(line.replace('\n', ''))

    # print(content_list)
    # print("\n\n")


def Hinglish_stop_words(words):
    all_words = []
    for w in words:
        if w.lower() not in content_list:
            all_words.append(w)

    return all_words


    # pattern = r'\b[a-zA-Z]+\b'  # Matches words containing only letters