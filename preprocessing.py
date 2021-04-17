#%%
from gensim.parsing import preprocessing

from reddit_scraper import test_comm, comments_as_list


prep_comment = preprocessing.preprocess_string(test_comm[0])
a = comments_as_list
prep_dok = preprocessing.preprocess_documents(a)
