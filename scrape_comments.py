import praw
import pandas as pd

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
for sub in sr.hot(limit=5):
    titles.append(sub.title)
    scores.append(sub.score)
    ratios.append(sub.upvote_ratio)
    comments.append(sub.comments)
    com_count.append(sub.num_comments)
    urls.append(sub.url)
    ids.append(sub.id)


df = pd.DataFrame(
    list(zip(titles, scores, ratios, comments, com_count, urls, ids)),
    columns=["title", "score", "ratio", "comments", "number_coms", "url", "id"])

# make dictionary for every submisson
comm_dict = {i:[] for i in ids}
# store list of comments to each submission in dictionary

for sub in sr.hot(limit=5):
    count = 0

    for comment in sub.comments.list():
        while count < len(ids):
            comm_dict[ids[count]].append(comment.body)count += 1
