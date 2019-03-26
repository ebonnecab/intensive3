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
