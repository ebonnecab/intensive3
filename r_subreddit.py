#! usr/bin/env python3
# Still need to write tests for these functions

#using python reddit api wrapper to make requests
def get_subreddit():
    import praw #pkg that connects to reddit api
    
    reddit = praw.Reddit(client_id='xxxxx', client_secret="xxxxx", user_agent='USERAGENT', username='xxxx', password='xxxx')

    # accessing prison reform subreddit
    subreddit = reddit.subreddit('prisonreform')

    #accessing hot category of subreddit
    hot_subreddit = subreddit.hot(limit=1000)

    return hot_subreddit

# created a dictionary of features for subreddit posts
def create_dict(hot_subreddit):

    topics_dict = {"title": [],
                   "id": [], 
                   "body": []}  

#iterating through chosen features of hot subreddit to append body of text to dict
    for submission in hot_subreddit:
        topics_dict["body"].append(submission.selftext)

    return topics_dict

def get_text(topics_dict):

#created empty lists for the text from each post
    corpus = []

#iterating through dict to append to list
    for text in topics_dict["body"]:
        corpus.append(text)
    
    return corpus

#opens a new file and writes each post from corpus to that file
def write_data(file, corpus):
    with open(file, 'w+') as f:
        f.write('\n Corpus\n')
        for post in corpus:
            f.write(post + "|")



if __name__ == '__main__':

    hot_reddit = get_subreddit()
    topics_dict = create_dict(hot_reddit)
    corpus = get_text(topics_dict)
    write_data('corpus.txt', corpus)



