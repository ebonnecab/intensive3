#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',client_id='QvAdTaUsIGkukg',client_secret="6ZT2FBooftzF3wA3I7d5XEzIayI",username='ebonnecab', password='Makeschool1!')

subreddit = reddit.subreddit('prisonreform')

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)


