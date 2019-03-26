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
