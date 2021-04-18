from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()

start_epoch = int(datetime.datetime(2021, 1, 1).timestamp())  # START DATE FROM WHERE OFF WE SCRAPE
end_epoch = int(datetime.datetime(2021, 3, 31).timestamp())

submissions = list(api.search_submissions(after=start_epoch, subreddit='wallstreetbets',
                                          filter=['url','author', 'title', 'subreddit']
                                          ))
# FILTER SUBMISSIONS THAT CONTAIN CASHTAG IN TITLE
for submission in submissions:
    words = submission.title.split()
    # print(words)
    cashtags = list(set(filter(lambda word: word.lower().startswith("$"), words)))
    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)

#%% SEARCH COMMENTS
# per day
# per subreddit
# per tag

subr = ['wallstreetbets', 'finance', 'pizza']
stocktags = ['$GME', '$BTC', '$AMC']

# make dictionary for every stocktag
sr_dict = {sr:[] for sr in subr}
comment_dict = {tag:[] for tag in stocktags}

# for sr in range(len(subr)):
#     subr_new = subr[sr]
#     new_dic = {}

for tag in stocktags:
    print(tag)
    wsb_search = api.search_comments(q=tag, subreddit=subr[0], after=start_epoch, before=end_epoch)

    max_response_cache = 10  # for testing, to be removed for real analysis
    cache = []  # for testing, to be removed for real analysis
    for c in wsb_search:
        cache.append(c)  # for testing, to be removed for real analysis
        comment_dict[tag].append(c.body)  # store body of comments in list in dictionary per tag

        # Omit this test to actually return all results. Wouldn't recommend it though: could take a while, but you do you.
        if len(cache) >= max_response_cache:  # for testing, to be removed for real analysis
            break




# #STORE EACH COMMENT AS LIST OBJECT IN A LIST
# wsb_comments = []
# i = 0
# while i < len(cache):
#     print(cache[i].body)
#     wsb_comments.append(cache[i].body)
#     i += 1

#%%
# import pandas as pd
# subr = ['wallstreetbets', 'finance', 'pizza']
# stocktags = ['$GME', '$BTC', '$AMC']
#
# frame = {'Day':[1,2,3], 'SR':subr, 'Tag':stocktags, 'comments':[3,2,1]}
#
# df = pd.DataFrame(frame)
