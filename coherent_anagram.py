"""Anagram maker."""
import random as r
import sys

with open("/usr/share/dict/words", 'r') as f:
    words = f.read()
    word_list = list(words.split("\n"))[:-1]  # [:-1] is to remove empty string


def pair(word):
    """Return dictionary of letters and count."""
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary


user_word = sys.argv[1]

filter_list = list(filter(lambda x: pair(x) == pair(user_word), word_list))
word_chooser = r.randint(0, len(filter_list) - 1)
print(filter_list[word_chooser])
