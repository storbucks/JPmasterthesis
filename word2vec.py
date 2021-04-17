#%%
import time
from gensim.models import Word2Vec as w2v

from reddit_scraper import splitted_comms_all

stime = time.time()
#%%
# comments to learn language model from
model = w2v(sentences=splitted_comms_all, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")

# model = w2v.load("word2vec.model")
# model.train([["hello", "world"]], total_examples=1, epochs=1)

vector = model.wv['up']
print(model.wv.similarity('bull', 'bear'))

print("Time: %s s" % ((time.time() - stime)))
