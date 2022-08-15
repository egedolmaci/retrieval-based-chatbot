from collections import Counter
from helpful_functions import preprocess, compare_overlap, check_sentence
import pandas as pd
from nltk.tokenize import word_tokenize

exit_commands = ("quit", "goodbye", "exit", "no")

class ChatBot:

  df = pd.read_csv('Mental_Health_FAQ.csv')  
  df['Clean'] = df['Questions'].apply(word_tokenize)
  flag = True

  def make_exit(self, user_message):
    for command in exit_commands:
      if command in user_message:
        print('Goodbye!')
        return True

  def chat(self):
      user_message = input('Hey! What would you like to know about mental health?\n> ')
      while not self.make_exit(user_message):
        if check_sentence(user_message):
          user_message = self.respond(user_message)
        else:
          print('Sorry, I did not understand.')
          self.chat()
        

  def find_intent_match(self, user_message):
      bow_user_message = Counter(preprocess(user_message))
      similarity_list = list()
      for i in self.df['Clean']:
        similarity_list.append(compare_overlap(bow_user_message, i))
      response_index = similarity_list.index(max(similarity_list))
      return response_index
    
  def respond(self, user_message):
    best_response = self.find_intent_match(user_message)
    response_to_use = self.df.at[best_response, 'Answers']
    print(response_to_use)
    input_message = input("> ")           
    return input_message

ege = ChatBot()

ege.chat()