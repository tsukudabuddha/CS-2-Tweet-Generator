from flask import Flask
import word_frequency
import stochastic_sampling
from clean_text import clean
app = Flask(__name__)


@app.route('/')
def start_page():
    return "Empty homescreen, go to /words for text"


@app.route('/words')
def home_page_text():
    clean_text = clean("joey_words.txt")
    histogram = word_frequency.histogram(clean_text)

    sentence = []
    for _ in range(0, 10):
        word = stochastic_sampling.main(histogram)
        sentence.append(word)
    string_sentence = " ".join(sentence)
    return string_sentence


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
