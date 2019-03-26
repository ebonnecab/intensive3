#load data file
filename = './v1.csv'
file = open(filename, 'rt')
text = file.read()
file.close()

#split text into word tokens
from nltk import word_tokenize
tokens = word_tokenize(text)

#remove non-alphabetic tokens
words = [word for word in tokens if word.isalpha()]
print(words[:100])