"""Anagram."""
import random as r
import sys


def anagram_gen(s):
    """Return scrambled word i.e. generate anagram."""
    anagram = []
    s = list(s)
    while len(s) > 0:
        ran_num = r.randint(0, len(s) - 1)
        letter = s[ran_num]
        anagram.append(letter)
        s.remove(letter)
    print("".join(anagram))


if __name__ == "__main__":
    word = sys.argv[1:]
    anagram_gen(word)
