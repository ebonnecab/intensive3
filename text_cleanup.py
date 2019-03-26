#load data file
filename = './v1.csv'
file = open(filename, 'rt')
text = file.read()
file.close()

#split text into sentences
from nltk import sent_tokenize
sentences = sent_tokenize(text)
print(sentences[0])