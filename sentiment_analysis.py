
#split text into word tokens
from nltk import word_tokenize
import string
from nltk.corpus import stopwords

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
    word_blob = ' '.join(words) #joined list to string to use text blob library
    
    blob = TextBlob(word_blob) #create blob object
    for word in blob.split(): #iterate over each word in string
        print(word)
        analysis = TextBlob(word) 
        print(analysis.sentiment) # determines polarity and subjectivity scores of each word
        if analysis.sentiment[0]>0: 
            print('Positive')
        elif analysis.sentiment[0]<0:
            print ('Negative')
        else:
            print ('Neutral')
    return

   
#import textblob library for simple NLP tasks
from textblob import TextBlob


if __name__ == '__main__': 
    sentiment()

