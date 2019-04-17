#! usr/bin/env python3

#still need to write tests! 

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

def stop_words(words):
    stop_words = set(stopwords.words('english'))
    #remove stop words from corpus
    clean_words = [w for w in words if not w in stop_words]
    
    return clean_words

#import textblob library for simple NLP tasks
from textblob import TextBlob

def get_sentiment(clean_words):
     #joined list to string to use text blob library
    word_blob = ' '.join(clean_words)
    blob = TextBlob(word_blob) #create blob object
    for word in blob.split():
        print(word)
        analysis = TextBlob(word)
        # determines polarity and subjectivity scores of each word
        print(analysis.sentiment)

    #categorizing words based upon sentiment value between -1 and 1
        if analysis.sentiment[0]>0: 
            print('Positive')
        elif analysis.sentiment[0]<0:
            print ('Negative')
        else:
            print ('Neutral')
        

if __name__ == '__main__':
    text = read_file('corpus.txt')
    tokens = get_tokens(text)
    clean_tokens = stop_words(tokens)
    final_analysis = get_sentiment(clean_tokens)
    print(final_analysis)
