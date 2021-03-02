"""
Description:
    config for the Scraper.py
"""

# create a reddit personal use script and enter the credentials here https://ssl.reddit.com/prefs/apps/
client_id = "xCoeA1iqMfQEsA"
client_secret = "G5hWvN2963eYFcsCxHFUq5sLENctIw"
bot_username = "bakingandfinance"

output_file = "scraped_data.pkl"
output_csv_file = "output.csv"

# UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
# Set unique id or subreddit
uniq_id = 'lvo9a9'

# override this in config to decide which attributes to save from a comment object
# def comment_to_list(comment):
#     return [comment.author, comment.body]