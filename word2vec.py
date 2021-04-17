#%%
import time
from gensim.models import Word2Vec as w2v

from reddit_scraper import splitted_comms_all, commis_all, comments_as_list


from gensim.parsing import preprocessing

from reddit_scraper import test_comm, comments_as_list


# prep_comment = preprocessing.preprocess_string(test_comm[0])
prep_dok = preprocessing.preprocess_documents(comments_as_list)

model = w2v(sentences=prep_dok, sg=1, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")

vector = model.wv['up']  # object essentially contains the mapping between words and embeddings (wv)
print(model.wv.similarity('up', 'high'))  # check similarity

# print("Time: %s s" % ((time.time() - stime)))
