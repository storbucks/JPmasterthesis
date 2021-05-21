#%%
import gensim
import numpy as np
import os
from gensim.utils import simple_preprocess
from gensim.parsing import preprocessing
from gensim import corpora
from gensim import models
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec

# tokenized comments as needed for gensim dictionary
from reddit_scraper import splitted_comms_all, commis_all, comments_as_list
#%%

# storing the extracted tokens into the dictionary
my_dictionary = corpora.Dictionary(splitted_comms_all)
print(my_dictionary)

# converting to a bag of word corpus
BoW_corpus =[my_dictionary.doc2bow(doc, allow_update = True) for doc in splitted_comms_all]
print(BoW_corpus)
#%%
# Word weight in Bag of Words corpus
word_weight =[]
for doc in BoW_corpus:
  for id, freq in doc:
    word_weight.append([my_dictionary[id], freq])
print(word_weight)

# create TF-IDF model
tfIdf = models.TfidfModel(BoW_corpus, smartirs='ntc')

# TF-IDF Word Weight
weight_tfidf = []
for doc in tfIdf[BoW_corpus]:
    for id, freq in doc:
        weight_tfidf.append([my_dictionary[id], np.around(freq, decimals=3)])
print(weight_tfidf)

#%%
# W2V model test
prep_dok = preprocessing.preprocess_documents(comments_as_list)
# list of words from all comments
data = commis_all
# We will split the data into two parts
data_1 = data[:60000]
data_2 = data[60000:]

# Create the Word2Vec model
w2v_model = Word2Vec(prep_dok, sg=1, vector_size=100, window=5, min_count=1, workers=4)
w2v_model.save('w2v_model_v2.model')
# similar words to the word "time"
print(w2v_model.wv.most_similar('time'))


#%%
# build model vocabulary from a sequence of sentences
w2v_model.build_vocab(data_2, update=True)

# train word vectors
w2v_model.train(data_2, total_examples=w2v_model.corpus_count, epochs=200)

print(w2v_model.wv['time'])
print(len(w2v_model.wv.index_to_key))  # number of unique words (after preprocessing) and thus vectors for NN