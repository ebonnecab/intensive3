#! usr/bin/env python3

import praw #pkg that connects to reddit api
import pandas as pd #pkg that handles/formats the data

#using python reddit api wrapper to make requests
reddit = praw.Reddit(user_agent='project-1 (by /u/ebonnecab)',client_id='QvAdTaUsIGkukg', client_secret="6ZT2FBooftzF3wA3I7d5XEzIayI", username='ebonnecab', password='Makeschool1!')

# accessing prison reform subreddit
subreddit = reddit.subreddit('prisonreform')


#accessing hot category of subreddit
hot_subreddit = subreddit.hot(limit=1000)

#accessing top category of subreddit
top_subreddit = subreddit.top(limit=1000)

# created an empty dictionary of features for top voted and hottest subreddit posts
topics_dict = {"title": [],
               "id": [], 
               "body": []}

topics_dict2 = {"title": [],
               "id": [],
               "body": []}

#iterating through chosen features and appending to dict
for submission in hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["body"].append(submission.selftext)

headers_list = []
text_list = []

for header in topics_dict["title"]:
    headers_list.append(header)

for text in topics_dict["body"]:
    text_list.append(text)


for submission in top_subreddit:
    topics_dict2["title"].append(submission.title)
    topics_dict2["body"].append(submission.selftext)


headers_list2 = []
text_list2 = []
i=0

for header in topics_dict2["title"]:
    headers_list2.append(header)

for text in topics_dict2["body"]:
    text_list2.append(text)
    
# print(text_list2)

dataframe = pd.DataFrame(headers_list)
dataframe['text_list'] = text_list
dataframe.columns = ["header", "texts"]
dataframe["texts"] = dataframe["texts"].apply(lambda x: x.replace('\n', ''))
# dataframe.to_csv('v1.csv', index=None)
# dataframe.head()

dataframe2 = pd.DataFrame(headers_list2)
dataframe2['text_list2'] = text_list2
dataframe2.columns = ["header", "texts"]
dataframe2["texts"] = dataframe["texts"].apply(lambda x: x.replace('\n', ''))
# dataframe2.to_csv('v2.csv', index=None)
dataframe = dataframe.append(dataframe2)
dataframe.to_csv('v1.csv', index=None)
