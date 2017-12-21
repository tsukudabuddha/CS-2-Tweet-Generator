from flask import Flask
import sys
sys.path.append('/Users/andrew/Documents/GitHub/CS-2-Tweet-Generator/source')

import markov_chain
app = Flask(__name__)


@app.route('/')
def start_page():
    return "Empty homescreen, go to /words for text"


@app.route('/words')
def home_page_text():
    with open("complete_corpus.txt", "r") as joey_file:
        text = joey_file.read()
    markov_dict = markov_chain.create_markov_dict(text)
    return markov_chain.markov_chain(markov_dict)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
