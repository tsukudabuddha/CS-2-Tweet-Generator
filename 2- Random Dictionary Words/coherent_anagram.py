"""Anagram maker."""
import random as r
import sys
import time

starting_time = time.time()

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
anagram = pair(user_word)
filter_list = list(filter(lambda x: pair(x) == anagram, word_list))
# Delete original word from list if inside
if user_word in filter_list:
    filter_list.remove(user_word)

ending_time = time.time()

if len(filter_list) != 0:
    word_chooser = r.randint(0, len(filter_list) - 1)
    print(filter_list[word_chooser])
    print("Total anagrams: " + str(len(filter_list)))
    print("Anagrams:")
    print(filter_list)
else:
    print("No anagrams for this word")

print("Time %f" % (ending_time - starting_time))