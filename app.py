from flask import Flask
import word_frequency
import stochastic_sampling
app = Flask(__name__)


@app.route('/')
def home_page_text():
    # histogram = word_frequency.histogram("joey_words.txt")
    histogram = word_frequency.histogram("one fish two fish red fish blue fish")
    sentence = []
    print("outside histo: " + str(histogram))
    for _ in range(0, 10):
        print("inside histo: " + str(histogram))
        word = stochastic_sampling.main(histogram)
        sentence.append(word)
    string_sentence = " ".join(sentence)
    return string_sentence


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
