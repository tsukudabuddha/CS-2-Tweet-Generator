

words = []
with open("phoebe_words.txt", 'r') as character_file:
    words.append(character_file.read())
with open("chandler_words.txt", 'r') as character_file:
    words.append(character_file.read())
with open("monica_words.txt", 'r') as character_file:
    words.append(character_file.read())
with open("ross_words.txt", 'r') as character_file:
    words.append(character_file.read())

with open("joey_words.txt", 'r') as character_file:
    words.append(character_file.read())
with open("rachel_words.txt", 'r') as character_file:
    words.append(character_file.read())
with open("complete_corpus.txt", "w") as corpus:
    corpus.write(" ".join(words))
