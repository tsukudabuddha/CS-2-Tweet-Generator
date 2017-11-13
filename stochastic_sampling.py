"""Return Stoichastiacally random word."""
import random as r


def total_count(histogram):
    """Return total number of words in histogram."""
    count = 0
    for key, value in histogram.items():
        count += value
    return count


def calculate_probablilites(histogram):
    """Calculate the probability per word and return histogram w/ values."""
    total = total_count(histogram)
    counter = 0
    new_histogram = {}
    for word, frequency in histogram.items():
        odds = (frequency / total)
        value = odds + counter
        new_histogram[word] = value
        counter += odds
    return new_histogram


def stochastic_sample(histogram):
    """Return randomly chosen item."""
    num_picker = r.random()
    for key, value in histogram.items():
        if num_picker < value:
            return key


def main(og_histogram):
    """thing."""
    probability_dict = calculate_probablilites(og_histogram)
    word = stochastic_sample(probability_dict)
    return word
