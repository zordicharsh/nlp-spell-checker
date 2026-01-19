import nltk
from spellchecker import SpellChecker
from nltk.corpus import words
# import pandas as pd



sentence = input("Enter a Sentence :")
sentence = sentence.lower()
tokens = nltk.word_tokenize(sentence)
dictionary = set(words.words())
print(dictionary)
print(tokens)
print(sentence)

misspelled = []

for word in tokens:
    if word.isalpha() and word not in dictionary:
        misspelled.append(word)

print("Misspelled words :" , misspelled)



