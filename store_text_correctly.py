from gensim.models.word2vec import Word2Vec
import pandas as pd
import numpy as np

## Load pretrained WE model
w2v_model = Word2Vec.load("w2v_model_v2.model")

## store as csv
df = pd.DataFrame(data=w2v_model.syn1neg)  # array of vectors
df.insert(loc=0, column="index", value=w2v_model.wv.index_to_key)  # add index in front
df.to_csv('embeddings.csv')  # to csv

## store as txt
arr = df.to_numpy()  # make df a ndarray
np.savetxt("embeddings.txt", arr, fmt="%s")  # ro txt, fmt = string
