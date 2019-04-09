# HOPE Data Analyis of Prison Reform Subreddit using Python

## Requirements
* Python 3
* IDE (Interactive Development Environment)
* PRAW (Python Reddit API Wrapper)
* Pandas library
* A reddit account
* Natural Language Toolkit
* Textblob library

## Part 1: Get Submissions from r/prisonreform

### Use Reddit API Wrapper to Make Request and Access Top Prison Reform Subreddit posts
Use Reddit Documentation to create an account and build an application with their API using the request below
``` Python
def get_subreddit():
    import praw #pkg that connects to reddit api
    reddit = praw.Reddit(config.user,client_id='xxxx', client_secret="xxxx", username='xxxx', password='xxxx')
    subreddit = reddit.subreddit('prisonreform')
    hot_subreddit = subreddit.hot(limit=1000)
    return hot_subreddit
```

### Create a Dictionary of Features for Subreddit posts
```Python
def create_dict(hot_subreddit):

    topics_dict = {"title": [],
                   "id": [], 
                   "body": []}  

#iterating through chosen features of hot subreddit to append body of text to dict
    for submission in hot_subreddit:
        topics_dict["body"].append(submission.selftext)

    return topics_dict

 ```

### Create a List from Topics_Dict to get a Corpus
```Python
def get_text(topics_dict):

#created empty lists for the text from each post
    corpus = []

#iterating through dict to append to list
    for text in topics_dict["body"]:
        corpus.append(text)
    
    return corpus
```
### Converted Corpus to Text File for Analysis
```Python
def write_data(file, corpus):
    with open(file, 'w+') as f:
        f.write('\n Corpus\n')
        for post in corpus:
            f.write(post + "|")

```
At this point you should have a txt file filled with posts from the subreddit. Before we can begin analyzing for sentiment we need to clean the text and split it into word tokens.
## Part Two: Tokenize Text and Do Sentiment Analysis

### Load Packages to Split Text into Word Tokens using NLTK (Natural Language Toolkit)
```Python
from nltk import word_tokenize
import string
from nltk.corpus import stopwords
```

### Read in Text File
```Python
def read_file(file):
    with open(file) as f:  # access file
        text = f.read()
    
    return text

```

### Tokenize and Clean the Text
I am using the Natural language toolkit to clean the text for better data analysis.
#### The first function tokenizes the words and strips them of punctuation and non-alphabetic characters
```Python
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

```
#### This function removes useless and extraneous words known as "stop words"
```Python
    def stop_words(words):
    stop_words = set(stopwords.words('english'))
    #remove stop words from corpus
    clean_words = [w for w in words if not w in stop_words]
    
    return clean_words
 ```
#### The last step uses the Textblob package to conduct sentiment analysis on word tokens
```Python
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
        

```

### Alternative Method to Conduct Sentiment Analysis and Plot Data
I wanted to show a visual representation of results and write them to a csv file so I used an alt method in sentiment_analysis2.py. The code is the same until the last step shown above.

#### Extra Packages needed
```Python
import pandas as pd #pkg that handles/formats the data
import matplotlib.pyplot as plt #pkg to plot data
```
#### The last step uses Textblob package and Matplotlib package to conduct sentiment analysis and plot results
```Python
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
 ```
Run in your fav text editor to see results :). Feel free to experiment with different subreddits!

### Sentiment Analysis on Prison Reform Subreddit
![alt text](https://github.com/ebonnecab/intensive3/blob/master/graphs/v2.png)
### Plans for future versions
* Expand for a more nuanced sentiment analysis
* Use R or Javascript to show visualization of data
* Refactor code
* Compare data across different corpus's

### Acknowledgements
All the tutorials, documentation, and repositories that helped me build this program
* https://machinelearningmastery.com/clean-text-machine-learning-python/
* https://medium.freecodecamp.org/how-to-build-a-twitter-sentiments-analyzer-in-python-using-textblob-948e1e8aae14
* https://medium.com/@rahulvaish/textblob-and-sentiment-analysis-python-a687e9fabe96
* https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/analyze-tweet-sentiments-in-python/
* https://github.com/aleszu/reddit-sentiment-analysis/blob/master/r_subreddit.py
* https://medium.com/@plog397/webscraping-reddit-python-reddit-api-wrapper-praw-tutorial-for-windows-a9106397d75e
* https://www.nltk.org/
* http://www.storybench.org/how-to-scrape-reddit-with-python/
* https://learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
* https://monkeylearn.com/sentiment-analysis/
* https://matplotlib.org/users/installing.html
