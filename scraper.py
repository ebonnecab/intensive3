#! usr/bin/env python3

import praw #pkg that connects to reddit api
import pandas as pd #pkg that handles/formats the data

#using python reddit api wrapper to make requests
reddit = praw.Reddit(user_agent='project-1 (by /u/ebonnecab)',client_id='QvAdTaUsIGkukg', client_secret="6ZT2FBooftzF3wA3I7d5XEzIayI", username='ebonnecab', password='Makeschool1!')

# accessing prison reform subreddit
subreddit = reddit.subreddit('prisonreform')


#accessing hot category of subreddit
hot_subreddit = subreddit.hot(limit=2)

#sample code that prints submission title and id of top submission
# for submission in subreddit.top(limit=1):
#     print(submission.title, submission.id)

# created an empty dictionary of features for top voted and hottest subreddit posts
topics_dict = {"title": [],
               "score": [],
               "id": [], 
               "url": [],
               "created": [],
               "body": []}

comm_list = []
header_list = []
i = 0
#iterating through chosen features and appending to dict
for submission in hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["id"].append(submission.id)
    topics_dict["body"].append(submission.selftext)

    while topics_dict["body"]:
        header_list.append(topics_dict["title"])
        comment = topics_dict["body"].pop(0)
        comm_list.append(comment)
        

print(header_list, comm_list)

# dataframe = pd.DataFrame(topics_dict)
# dataframe.columns = ['']

# d = pd.read_csv(r'./v1.csv')
