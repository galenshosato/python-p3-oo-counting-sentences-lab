#!/usr/bin/env python3
class MyString:
    def __init__(self, value = ""):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
      if type(value) == str:
          self._value = value
      else:
        print("The value must be a string.")
    
    value = property(get_value, set_value) 
    
    def is_sentence(self):
      return self._value[-1] == '.'
    
    def is_question(self):
      return self._value[-1] == '?'
    
    def is_exclamation(self):
      return self._value[-1] == '!'
    
    def count_sentences(self):
      new_value = self._value.replace("?", "." )
      new_value = new_value.replace("!", ".")
      new_value = new_value.split(".")
      new_value = [i for i in new_value if i]
      return len(new_value) 


      
      


     
