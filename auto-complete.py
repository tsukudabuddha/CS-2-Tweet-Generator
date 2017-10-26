"""Auto-complete Program."""
import sys

with open("/usr/share/dict/words", 'r') as f:
    words = f.read()
    word_list = list(words.split("\n"))[:-1]  # [:-1] is to remove empty string

user_input = sys.argv[1]
chars = user_input

finish_list = list(filter(lambda x: x[:len(chars)] == chars, word_list))
print("\n".join(finish_list))
