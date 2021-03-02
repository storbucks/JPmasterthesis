import praw
import pandas as pd

# gain acces through api
reddit = praw.Reddit(
    user_agent="comment_scrape",
    client_id="xCoeA1iqMfQEsA",
    client_secret="G5hWvN2963eYFcsCxHFUq5sLENctIw",
    username="bakingandfinance",
    # password="hf)ua7(:ski9@1",
)

# submission id found in URL
url = "https://www.reddit.com/r/finance/comments/lvo9a9/gamestop_surges_more_than_18_other_meme_stocks/"
submission = reddit.submission(url=url)

# scrape comments
comments = []
for top_level_comment in submission.comments:
    comments.append(str(top_level_comment.body))

c = pd.DataFrame(comments, columns=["comments"])



