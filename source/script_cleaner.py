"""Script Cleaner."""
import re
import web_scraper as ws

def clean_text(text_file):
    with open(text_file, "r") as text_file:
        words = text_file.read()
    character_sentences = re.findall("(?<=Phoebe:)(.*?)(?=\n)", words)
    character_sentences = re.sub(r'[^\w]', ' ', " ".join(character_sentences))
    words = character_sentences.split(" ")
    word_list = []
    for word in words:
        stripped_word = word.strip()
        if stripped_word is not "":
            if len(stripped_word) == 1:
                if stripped_word == "I":
                    word_list.append(stripped_word)
            else:
                word_list.append(word)

    with open("phoebe_words.txt", 'w') as character_file:
        character_file.write(" ".join(word_list))
    return word_list


if __name__ == "__main__":
    print(clean_text("messy_corpus.txt"))
