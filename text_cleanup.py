#load data file
filename = './v1.csv'
file = open(filename, 'rt')
text = file.read()
file.close()

#split text into word tokens
from nltk import word_tokenize
tokens = word_tokenize(text)

#convert tokens to lowercase
tokens = [word.lower() for word in tokens]

#removes punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

#remove non-alphabetic tokens
words = [word for word in stripped if word.isalpha()]

#remove stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

#joined list to string to use text blob library
word_blob = ' '.join(words)

from textblob import TextBlob

blob = TextBlob(word_blob)

print(blob.sentiment)

# for ngram in blob.ngrams(2):
#     print (ngram)
#using pandas to write tokens to new csv file
# import pandas as pd 
# dataframe = pd.DataFrame(words)
# dataframe.columns=["text"]
# dataframe["text"] = dataframe["text"].apply(lambda x: x.replace('\n', ''))
# dataframe.to_csv('v2.csv', index=None)


# print(blob)

# print(blob)

