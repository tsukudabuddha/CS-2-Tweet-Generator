"""Random dictionary words."""
import random as r
import time


def create_word_list():
    """Return list of words in dictionary."""
    with open("/usr/share/dict/words", 'r') as f:
        words = f.read()
        words.strip()  # Remove whitespaces from beginning and end of file
        word_list = list(words.split("\n"))
    return word_list


def create_sentence(word_list):
    """Return sentence of randomly picked words.

    Take in list of words to pick from
    """
    word_count = r.randint(5, 10)  # Randomly choose length of sentence
    sentence_list = []
    for _ in range(0, word_count):
        index = r.randint(0, len(word_list) - 1)
        sentence_list.append(word_list[index])
    sentence = " ".join(sentence_list)
    return sentence


if __name__ == "__main__":
    word_list = create_word_list()
    starting_time = time.time()
    sentence = create_sentence(word_list)
    ending_time = time.time()
    print(sentence)
    print("Took %f seconds" % (ending_time - starting_time))
