#%%
import time
from gensim.models import Word2Vec as w2v

from preprocessing import prep_dok  # comments to learn language model from

# stime = time.time()
#%%

model = w2v(sentences=prep_dok, sg=1, vector_size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")

vector = model.wv['up']  # object essentially contains the mapping between words and embeddings (wv)
print(model.wv.similarity('up', 'high'))  # check similarity

# print("Time: %s s" % ((time.time() - stime)))
