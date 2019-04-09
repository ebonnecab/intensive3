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

def stop_words(words):
    stop_words = set(stopwords.words('english'))
    #remove stop words from corpus
    clean_words = [w for w in words if not w in stop_words]
    
    return clean_words

#import textblob library for simple NLP tasks
from textblob import TextBlob
import pandas as pd #pkg that handles/formats the data
import matplotlib.pyplot as plt #pkg to plot data

def get_sentiment(clean_words):
    
    #alternative method for getting sentiment values
    sentiment_objects = [TextBlob(w) for w in clean_words]
    sentiment_objects[0].polarity, sentiment_objects[0]

    # Create list of polarity valuesx and tweet text
    sentiment_values = [[w.sentiment.polarity, str(w)] for w in sentiment_objects]
    sentiment_values[0]

    # Create dataframe containing the polarity value and words
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "word"])

    # Remove polarity values equal to zero for visual purposes
    sentiment_df = sentiment_df[sentiment_df.polarity != 0]
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot histogram with break at zero
    sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
    ax=ax, color="purple")

    plt.title("Sentiments from Prison Reform Subreddit")
    plt.show()

    #Write dataframe to csv
    # sentiment_df.to_csv('csv-files/v4.csv', index=None)


if __name__ == '__main__': 
    text = read_file('corpus.txt')
    tokens = get_tokens(text)
    clean_tokens = stop_words(tokens)
    analysis = get_sentiment(clean_tokens)