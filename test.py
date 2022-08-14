import pandas as pd
from helpful_fucntions import compare_overlap
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from collections import Counter

def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    return(tokens)

df = pd.read_csv('./Mental_Health_FAQ.csv')


df['Clean'] = df['Questions'].apply(word_tokenize)

user_message = preprocess('What is mental health?')


def find_intent_match(user_message):
      bow_user_message = Counter(user_message)
      similarity_list = list()
      for i in df['Clean']:
        similarity_list.append(compare_overlap(bow_user_message, i))
      response_index = similarity_list.index(max(similarity_list))
      print(len(similarity_list))
      return response_index

print(find_intent_match(user_message))

