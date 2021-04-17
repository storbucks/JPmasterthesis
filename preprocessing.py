#%%
from gensim.parsing import preprocessing

from reddit_scraper import test_comm



prep_comment = preprocessing.preprocess_string(test_comm[0])
print(prep_comment)