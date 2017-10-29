"""Re-Arrange inputted words."""
import random as r
import sys


def scramble_sentence(words):
    """Scramble sentence."""
    line = []
    while len(words) > 0:
        index = r.randint(0, len(words) - 1)
        line.append(words[index])
        words.remove(words[index])
    return " ".join(line)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(scramble_sentence(arguments))
