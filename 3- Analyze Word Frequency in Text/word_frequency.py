"""Word Frequency."""


def histogram(source_text):
    """Return dictionary of words and histogram."""
    histogram = {}
    text = source_text.split(" ")
    for word in text:
        word = word.lower()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    """Return number of unique_words in histogram."""
    return len(histogram)


def frequency(word, histogram):
    """Return word frequency in histogram."""
    return histogram[word]


if __name__ == "__main__":
    text = "one fish two fish red fish blue fish"
    print(histogram(text))
