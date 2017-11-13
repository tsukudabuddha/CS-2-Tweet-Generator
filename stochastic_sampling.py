"""Return Stoichastiacally random word."""
import random as r
import time


def total_count(histogram):
    count = 0
    for key, value in histogram.items():
        count += value
    return count


def calculate_probablilites(histogram):
    total = total_count(histogram)
    print("total = " + str(total))
    counter = 0
    new_histogram = {}
    for word, frequency in histogram.items():
        odds = (frequency / total)
        print("odds " + str(odds))
        value = odds + counter
        new_histogram[word] = value
        counter += odds
    print("new histo: " + str(new_histogram))
    return new_histogram


def stochastic_sample(histogram):
    """Return randomly chosen item."""
    num_picker = r.random()
    print("ssh: " + str(histogram))
    for key, value in histogram.items():
        if num_picker < value:
            return key


def main(og_histogram):
    """thing."""
    print(og_histogram)
    probability_dict = calculate_probablilites(og_histogram)
    print("prob :" + str(probability_dict))
    word = stochastic_sample(probability_dict)
    print("word" + str(word))
    return word
