
#split text into word tokens
from nltk import word_tokenize
import string
from nltk.corpus import stopwords
   
#import textblob library for simple NLP tasks
from textblob import TextBlob

#function for sentiment analysis
def sentiment():
    #load data file
    filename = './v1.csv'
    file = open(filename, 'rt')
    text = file.read()
    file.close()

    tokens = word_tokenize(text) #split text into word tokens
    tokens = [word.lower() for word in tokens] #converts tokens to lowercase   
    table = str.maketrans('', '', string.punctuation) #removes punctuation from each word
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()] #remove non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words] #remove stop words from corpus
    # word_blob = ' '.join(words) #joined list to string to use text blob library
    
    sentiment_objects = [TextBlob(w) for w in words]
    sentiment_objects[0].polarity, sentiment_objects[0]

    # Create list of polarity valuesx and tweet text
    sentiment_values = [[w.sentiment.polarity, str(w)] for w in sentiment_objects]
    sentiment_values[0]

    import pandas as pd #pkg that handles/formats the data

    # Create dataframe containing the polarity value and tweet text
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "word"])

    #Write datafram to csv
    sentiment_df.to_csv('v3.csv', index=None)


if __name__ == '__main__': 
    sentiment()
