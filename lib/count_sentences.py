#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=''):
    self._value = value

  def is_sentence(self):
    return self._value.endswith(".")

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    sentences = [s.strip() for s in re.split(r'[.!?]', self._value) if s.strip()]
    return len(sentences)

  value = property(get_value, set_value)