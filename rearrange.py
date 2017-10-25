"""Re-Arrange inputted words."""
import random as r
import sys

if __name__ == "__main__":
    words = sys.argv[1:]
    line = []
    while len(words) > 0:
        index = r.randint(0, len(words) - 1)
        line.append(words[index])
        words.remove(words[index])
    print(" ".join(line))
