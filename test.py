import pandas as pd
from helpful_fucntions import compare_overlap
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    return(tokens)

df = pd.read_csv('./Mental_Health_FAQ.csv')
user_message = preprocess('Hello everyone my name is Ege')

df['Clean'] = df['Questions'].apply(word_tokenize)
similarity_list = list()
for i in df['Clean']:
    similarity_list.append(compare_overlap(user_message, i))

print(similarity_list)

