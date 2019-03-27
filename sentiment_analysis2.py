
#split text into word tokens
from nltk import word_tokenize
import string
from nltk.corpus import stopwords

#pkg to plot data
import matplotlib.pyplot as plt
   
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
    
    #alternative method for getting sentiment values
    sentiment_objects = [TextBlob(w) for w in words]
    sentiment_objects[0].polarity, sentiment_objects[0]

    # Create list of polarity valuesx and tweet text
    sentiment_values = [[w.sentiment.polarity, str(w)] for w in sentiment_objects]
    sentiment_values[0]

    import pandas as pd #pkg that handles/formats the data

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

    # #Write datafram to csv
    # sentiment_df.to_csv('v3.csv', index=None)


if __name__ == '__main__': 
    sentiment()
