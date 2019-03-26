# HOPE Data Analyis of Prison Reform Subreddit using Python

## Requirements
* Python 3
* IDE (Interactive Development Environment)
* PRAW (Python Reddit API Wrapper)
* Pandas
* A reddit account
* Natural Language Toolkit
* Textblob library

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
