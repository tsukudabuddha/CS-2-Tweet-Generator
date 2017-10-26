"""Anagram."""
import random as r


def anagram_gen(s):
    anagram = []
    s = list(s)
    while len(s) > 0:
        ran_num = r.randint(0, len(s) - 1)
        letter = s[ran_num]
        anagram.append(letter)
        s.remove(letter)
    print("".join(anagram))


anagram_gen("Andrew")
