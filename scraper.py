#! usr/bin/env python3

import praw #pkg that connects to reddit api
import pandas as pd #pkg that handles/formats the data
import datetime as dt

#using python reddit api wrapper to make requests
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',client_id='QvAdTaUsIGkukg',client_secret="6ZT2FBooftzF3wA3I7d5XEzIayI",username='ebonnecab', password='Makeschool1!')

#accessing prison reform subreddit
subreddit = reddit.subreddit('prisonreform')

#accessing hot subreddit
python_subreddit = subreddit.hot(limit=1000)

#accessing top-500 submissions in r/prisonreform
top_subreddit = subreddit.top(limit=500)

#sample code that prints submission title and id of top submission
# for submission in subreddit.top(limit=1):
#     print(submission.title, submission.id)

# created an empty dictionary of features
topics_dict = {"title": [],
               "subreddit": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

#iterating through chosen features and appending to dict
for submission in python_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict['subreddit'].append(submission.subreddit)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

print(topics_dict)
