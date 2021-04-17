import praw
import pandas as pd
import time

from datetime import datetime

start_time = time.time()

# API access
reddit = praw.Reddit(
    user_agent="comment_scrape",
    client_id="xCoeA1iqMfQEsA",
    client_secret="G5hWvN2963eYFcsCxHFUq5sLENctIw",
    username="bakingandfinance",
    # password="hf)ua7(:ski9@1",
)
# list of subreddits to examine to automate it or write code for each sr to keep structure understandable and organized?
sr = reddit.subreddit("finance")

dates = []
titles = []
selftext = []
scores = []
ratios = []
comments = []
com_count = []
urls = []
ids = []
# for every submission in given subreddit, extract data as shown and extract comment tree in separate
for subm in sr.new(limit=50):  # newest
    dates.append(datetime.utcfromtimestamp(int(subm.created_utc)).strftime('%Y-%m-%d %H:%M:%S'))
    titles.append(subm.title)
    selftext.append(subm.selftext)
    scores.append(subm.score)
    ratios.append(subm.upvote_ratio)
    comments.append(subm.comments)
    com_count.append(subm.num_comments)
    urls.append(subm.url)
    ids.append(subm.id)

# store scraped info in dataframe
df = pd.DataFrame(
    list(zip(dates, titles, selftext, scores, ratios, comments, com_count, urls, ids)),
    columns=["date", "title", "selftext", "score", "ratio", "comments", "number_coms", "url", "id"])
#%%
# make dictionary for every submisson
comms_dict = {i:[] for i in ids}
tot_comms = []
for id in ids:
    submission = reddit.submission(id=id)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comms_dict[id].append(comment.body)
    tot_comms.append(len(comms_dict[id]))
print("Total comments scraped: %s" % sum(tot_comms))
print("Time: %s min" % ((time.time() - start_time)/60))

# list of sentences or rather list of words in correct order needed to train word2vec: CHECK!!!
#%%
import itertools
splitted_comms_all = []
for id in ids:
    test_comm = comms_dict.get(id)  # gets list of resp. submission
    join_comm = "".join(test_comm) # makes list to string
    split_comm = join_comm.split()  # list of words
    splitted_comms_all.append(split_comm) # makes list of list of words
commis_all = list(itertools.chain.from_iterable(splitted_comms_all))  # joins lists inside list
# attention: connection to submission ID lost (is it even needed though?)
ratio = len(commis_all)/sum(tot_comms)
print("Avg. words per comment: %s" % ratio)