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
for subm in sr.hot(limit=10):
    titles.append(subm.title)
    scores.append(subm.score)
    ratios.append(subm.upvote_ratio)
    comments.append(subm.comments)
    com_count.append(subm.num_comments)
    urls.append(subm.url)
    ids.append(subm.id)


df = pd.DataFrame(
    list(zip(titles, scores, ratios, comments, com_count, urls, ids)),
    columns=["title", "score", "ratio", "comments", "number_coms", "url", "id"])

# make dictionary for every submisson
comm_dict = {i:[] for i in ids}
for id in ids:
    submission = reddit.submission(id=id)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comm_dict[id].append(comment.body)
