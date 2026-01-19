import nltk
from nltk.corpus import words
# import pandas as pd



sentence = input("Enter a Sentence :")
sentence = sentence.lower()
tokens = nltk.word_tokenize(sentence)
dictionary = set(words.words())

print(tokens)
print(sentence)

misspelled = []

for word in tokens:
    if word.isalpha() and word not in dictionary:
        misspelled.append(word)


print("Misspelled words :" , misspelled)


def get_suggestions(word,disctionary,max=3):
    suggestion=[]

    for dict_word in disctionary:
        distance = nltk.edit_distance(word,dict_word)
        if distance <= 2:
            suggestion.append((dict_word, distance))
    suggestion = sorted(suggestion, key=lambda x: x[1])
    return [w for w, d in suggestion[:max]]
    



for word in misspelled:
    suggestion = get_suggestions(word,dictionary)
    print(f"Suggestions for '{word}':{suggestion} ")






