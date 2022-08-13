from collections import Counter
from helpful_fucntions import preprocess, compare_overlap
import pandas as pd

exit_commands = ("quit", "goodbye", "exit", "no")

class ChatBot:

  df = pd.read_csv('Mental_Health_FAQ.csv')  

  def make_exit(self, user_message):
    for command in exit_commands:
      if command in user_message:
        print('Goodbye!')
        return True

  def chat(self):
    user_message = input('Hey! What would you like to know about our menu?\n')
    while not self.make_exit(user_message):
      user_message = self.respond(user_message)

  def find_intent_match(self, responses, user_message):
      bow_user_message = Counter(preprocess(user_message))
      processed_responses = [Counter(preprocess(response)) for response in responses]
      similarity_list = [compare_overlap(doc, bow_user_message) for doc in processed_responses]
      response_index = similarity_list.index(max(similarity_list))
      return responses[response_index]
    
  def respond(self, user_message):
    best_response = self.find_intent_match(user_message)
    print(best_response)
    input_message = input("Do you have any other questions? ")           
    return input_message

ege = ChatBot()

ege.chat()
