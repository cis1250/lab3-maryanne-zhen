#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# -- MAIN PROGRAM ---

# Ask user to enter a sentence
user_sentence = input("Enter a sentence: ")

# Prompt user again if given input is not a sentene
while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Splitting the sentence
sentence = (user_sentence.lower()).split()

# Removing punctuation from the sentence
for wd in sentence: # go through each item
  for ch in wd: # go through each character in the sentence
    if ch in '[,.!?]':
      sentence[sentence.index(wd)] = wd.replace(ch, "")

# Creating two empty lists for words and frequencies
words = []
frequencies = []

# Counting words
for wd in sentence: # go through all words in sentence
  if wd in words:
    # if word already exists in the list, add to counter
    ind = words.index(wd)
    frequencies[ind] += 1
  else:
    # if word does not exist in the list, add it to the list and start a counter
    words.append(wd)
    frequencies.append(1)

# Print the results
for i in range(len(words)):
  print(f"{words[i]:10} : {frequencies[i]:5}")
