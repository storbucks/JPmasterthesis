from gensim.models.word2vec import Word2Vec
import pandas as pd
import numpy as np
import textblob as tb
import nltk

## Load pretrained WE model
import reddit_scraper

# w2v_model = Word2Vec.load("w2v_model_v2.model")

positive_blob = tb.TextBlob("I really enjoy performing NLP with TextBlob")
print(positive_blob.sentiment.polarity)

from reddit_scraper import titles
#%%
sent = tb.TextBlob("I'm happy to be here")
print(sent.sentiment.polarity)

# check senitment score per title --> make for comments and around stock titles
titles_sentiment = []
for i in range(len(titles)):
    sent = tb.TextBlob(titles[i])
    titles_sentiment.append(sent.sentiment.polarity)

#%%
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
#%%
import torch
x = torch.rand(5, 3)
print(x)
