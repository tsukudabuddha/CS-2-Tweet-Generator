"""Random dictionary words."""
import random as r
import time

starting_time = time.time()

with open("/usr/share/dict/words", 'r') as f:
    words = f.read()
    word_list = list(words.split("\n"))[:-1]  # [:-1] is to remove empty string

word_count = r.randint(5, 10)  # Randomly choose length of sentence
sentence_list = []
for _ in range(0, word_count):
    index = r.randint(0, len(word_list) - 1)
    sentence_list.append(word_list[index])
sentence = " ".join(sentence_list)

ending_time = time.time()

print(sentence)
print("Took %f seconds" % (ending_time - starting_time))
