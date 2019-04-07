#! usr/bin/env python3

#split text into word tokens
from nltk import word_tokenize
import string
from nltk.corpus import stopwords

def read_file(file):
    with open(file) as f:  # access file
        text = f.read()
    
    return text

def get_tokens(text):
    #split text into word tokens
    tokens = word_tokenize(text)
    #converts tokens to lowercase
    tokens = [word.lower() for word in tokens]
    #removes punctuation from each word
    table = str.maketrans('', '', string.punctuation) 
    stripped = [w.translate(table) for w in tokens]
    #remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]

    return words

if __name__ == '__main__':
    text = read_file('corpus.txt')
    tokens = get_tokens(text)
    print(tokens)