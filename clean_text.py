"""Clean text Script."""
import re
#  TODO: account for parenthesis and stage cues


def clean(source_name):
    """Take in ugly string and return clean one."""
    with open(source_name, 'r') as f:
        text = f.read()
    text_list = re.split('; |, |\n| |\!|\?', text)
    if '' in text_list:
        text_list = list(filter(lambda x: x != " " and x != "", text_list))
    return text_list


if __name__ == "__main__":
    # Using as a test
    clean("joey_words.txt")
