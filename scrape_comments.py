import praw
import pandas as pd
import time

start_time = time.time()

# API access
reddit = praw.Reddit(
    user_agent="comment_scrape",
    client_id="xCoeA1iqMfQEsA",
    client_secret="G5hWvN2963eYFcsCxHFUq5sLENctIw",
    username="bakingandfinance",
    # password="hf)ua7(:ski9@1",
)
# # list of subreddits to examine to automate it or write code for each sr to keep structure understandable and organized?
# srs = ["finance", "wallstreetbets"]
# # access subreddit
# for i in srs:
#     sr = reddit.subreddit(i)
#     print(sr)

sr = reddit.subreddit("finance")

titles = []
scores = []
ratios = []
com_count = []
comments = []
urls = []
ids = []
# for every submission in given subreddit, extract data as shown and extract comment tree in separate 
for subm in sr.new(limit=100):  # newest
    titles.append(subm.title)
    scores.append(subm.score)
    ratios.append(subm.upvote_ratio)
    comments.append(subm.comments)
    com_count.append(subm.num_comments)
    urls.append(subm.url)
    ids.append(subm.id)

# store scraped info in dataframe
df = pd.DataFrame(
    list(zip(titles, scores, ratios, comments, com_count, urls, ids)),
    columns=["title", "score", "ratio", "comments", "number_coms", "url", "id"])

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

# list of sentences or rather list of words in correct order needed to train word2vec: CHECK!!!


print("Time: %s sec" % (time.time() - start_time))
