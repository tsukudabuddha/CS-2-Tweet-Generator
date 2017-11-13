"""Word Frequency."""


def histogram(text):
    """Return dictionary of words and frequecy."""
    histogram = {}
    for word in text:
        word = word.lower()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def histogram_nested_lists(source_text):
    """Return nested lists of words and frequecy."""
    source_text = source_text.lower()
    text = source_text.split(" ")
    histogram = []
    for word in text:
        create_new_entry = True
        for entry in histogram:
            if entry[0] == word:
                entry[1] += 1
                create_new_entry = False
                break

        if create_new_entry:
            histogram.append([word, 1])
    return histogram


def histogram_list_tuples(source_text):
    """Return a list of tuples."""
    source_text = source_text.lower()
    text = source_text.split(" ")
    histogram = []

    for word in text:
        create_new_entry = True
        for entry in histogram:
            if entry[0] == word:
                num = entry[1] + 1
                histogram.remove(entry)
                histogram.append((word, num))
                create_new_entry = False
                break

        if create_new_entry:
            histogram.append((word, 1))
    return histogram


def unique_words(histogram):
    """Return number of unique_words in histogram."""
    return len(histogram)


def frequency(word, histogram):
    """Return word frequency in histogram."""
    return histogram[word]


if __name__ == "__main__":
    text = "one fish two fish red fish blue fish"
    print(histogram_list_tuples(text))
