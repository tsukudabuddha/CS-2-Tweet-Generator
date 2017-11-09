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
    counter = 0
    for word, frequency in histogram.items():
        odds = (frequency / total)
        value = odds + counter
        histogram[word] = value
        counter += odds
    return histogram


def stochastic_sample(histogram):
    """Return randomly chosen item."""
    num_picker = r.random()
    for key, value in histogram.items():
        if num_picker < value:
            return key


if __name__ == "__main__":
    og_histogram = {"one": 1, "fish": 4, "two": 1, "blue": 1, "red": 1}
    probability_dict = calculate_probablilites(og_histogram)
    words = []
    histogram = {}
    starting_time = time.time()
    for _ in range(0, 100000):
        words.append(stochastic_sample(probability_dict))
    ending_time = time.time()

    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    print(histogram)
    print("Time took %f" % (ending_time - starting_time))
