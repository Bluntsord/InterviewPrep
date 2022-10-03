from typing import *

def countSentences(wordSet, sentences):
    word_dict = {}
    for word in wordSet:
        curr_word = [a for a in word]
        curr_word.sort()
        curr_word = "".join(curr_word)
        word_dict[curr_word] = word_dict.get(curr_word, 0) + 1

    number_dict = {}
    for word in sentences.split(" "):
        curr_word = [a for a in word]
        curr_word.sort()
        curr_word = "".join(curr_word)
        number_dict[curr_word] = number_dict.get(curr_word, 0) + 1

    curr = 1
    for word, number in number_dict.items():
        curr *= (number ** word_dict.get(word, 1))

    return curr

wordSet = ["listen", "silent", "it", "is"]
sentences = "listen is is silent"
print(countSentences(wordSet, sentences))

