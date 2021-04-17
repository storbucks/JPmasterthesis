#%%
import gensim
import numpy as np
import os
from gensim.utils import simple_preprocess
from gensim.parsing import preprocessing
from gensim import corpora

from reddit_scraper import test_comms, comments_as_list


# storing the extracted tokens into the dictionary
my_dictionary = corpora.Dictionary(test_comms)
print(my_dictionary)

# convertig to a bag of word corpus
BoW_corpus =[my_dictionary.doc2bow(doc, allow_update = True) for doc in test_comms]
print(BoW_corpus)
