# HOPE Data Analyis of Prison Reform Subreddit using Python

## Requirements
* Python 3
* IDE (Interactive Development Environment)
* PRAW (Python Reddit API Wrapper)
* Pandas
* A reddit account
* Natural Language Toolkit
* Textblob library

## Part 1: Get Corpus from r/prisonreform

### Use Reddit API Wrapper to make requests
Use Reddit Documentation to create an account and build an application with their API using the request below
``` Python
reddit = praw.Reddit(config.user,client_id='xxxx', client_secret="xxxx", username='xxxx', password='xxxx')
```
### Access Top and Hottest Prison Reform Subreddit posts
```Python
subreddit = reddit.subreddit('prisonreform')
hot_subreddit = subreddit.hot(limit=1000)
top_subreddit = subreddit.top(limit=1000)
```
### Create an empty dictionary of features for Subreddit posts
```Python
topics_dict = {"title": [],
               "id": [], 
               "body": []}

topics_dict2 = {"title": [],
               "id": [],
               "body": []}
 ```
 ### Iterate through chosen features of hot and top subreddit to append to dict
 ```Python
 for submission in hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["body"].append(submission.selftext)

for submission in top_subreddit:
    topics_dict2["title"].append(submission.title)
    topics_dict2["body"].append(submission.selftext)
```
### Create an empty list for headers and text and iterate through dict to append to lists
```Python
headers_list = []
text_list = []

headers_list2 = []
text_list2 = []

for header in topics_dict["title"]:
    headers_list.append(header)

for text in topics_dict["body"]:
    text_list.append(text)

for header in topics_dict2["title"]:
    headers_list2.append(header)

for text in topics_dict2["body"]:
    text_list2.append(text)
```
### Import pandas package to handle/format data and convert list to panda data frame
```Python
import pandas as pd

dataframe = pd.DataFrame(headers_list)
dataframe['texts'] = text_list
dataframe.columns = ["header", "texts"]
dataframe["texts"] = dataframe["texts"].apply(lambda x: x.replace('\n', ''))

dataframe2 = pd.DataFrame(headers_list2)
dataframe2['texts'] = text_list2
dataframe2.columns = ["header", "texts"]
dataframe2["texts"] = dataframe2["texts"].apply(lambda x: x.replace('\n', ''))

dataframe = dataframe.append(dataframe2)
```
### Write Dataframe to CSV for analysis
``` Python
dataframe.to_csv('v1.csv', index=None)
```
At this point you should have a CSV file filled with text and headers from the subreddit posts. Before we can begin analyzing for sentiment we need to clean the text and split it into word tokens.
## Part Two: Tokenize Text and Do Sentiment Analysis

### Load Packages to Split Text into Word Tokens using NLTK (Natural Language Toolkit)
```Python
from nltk import word_tokenize
import string
from nltk.corpus import stopwords
```

### Import Textblob Library for simple NLP(Natural Language Processing) tasks
```Python
from textblob import TextBlob
```

### Sentiment Analysis Function
I wrapped this script into one big function but I plan to split into smaller functions to make code more modular.
#### The first part of the function loads in the csv file
```Python
def sentiment():
    #load data file
    filename = './v1.csv'
    file = open(filename, 'rt')
    text = file.read()
    file.close()
```
#### The next step tokenizes the corpus by stripping away extraneous/non-alphabetical characters, stop words, and joining list to a string to use in text blob library
```Python
    tokens = word_tokenize(text) #split text into word tokens
    tokens = [word.lower() for word in tokens] #converts tokens to lowercase   
    table = str.maketrans('', '', string.punctuation) #removes punctuation from each word
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()] #remove non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words] #remove stop words from corpus
    word_blob = ' '.join(words) #joined list to string to use text blob library

    blob = TextBlob(word_blob) #create blob object
 ```
#### The last step uses the Textblob package to conduct sentiment analysis on word tokens
```Python
for word in blob.split(): #iterate over each word in string
        print(word)
        analysis = TextBlob(word) 
        print(analysis.sentiment) # determines polarity and subjectivity scores of each word
        
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
#pkg to plot data
import matplotlib.pyplot as plt
```
#### The last step uses Textblob package and Matplotlib package to conduct sentiment analysis and plot results
```Python
#alternative method for getting sentiment values
    sentiment_objects = [TextBlob(w) for w in words]
    sentiment_objects[0].polarity, sentiment_objects[0]

    # Create list of polarity valuesx and tweet text
    sentiment_values = [[w.sentiment.polarity, str(w)] for w in sentiment_objects]
    sentiment_values[0]

    import pandas as pd #pkg that handles/formats the data

    # Create dataframe containing the polarity value and tweet text
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
![alt text](https://github.com/ebonnecab/intensive3/blob/master/graphs/V1_graph.png)
### Plans for future versions
* Expand for a more nuanced sentiment analysis
* Use R to show visualization of data
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
