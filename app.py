from flask import Flask
import word_frequency
import stochastic_sampling
app = Flask(__name__)


@app.route('/')
def home_page_text():
    histogram = word_frequency.histogram("joey_words.txt")
    sentence = ""
    for _ in range(0, 10):
        sentence.append(stochastic_sampling.stochastic_sample(histogram))
    return sentence


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
