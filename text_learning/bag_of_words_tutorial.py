# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

string1 = "hi Katie the self driving car will be late Best Sebastian" 

string2 = "Hi Sebastian the machine learning class will be great great great Best Katie" 

string3 = "Hi Katie the machine learning class will be most excellent" 

email_list = [string1, string2, string3]

#%%
# Fit 
bag_of_words = vectorizer.fit(email_list)

# Transform
bag_of_words = vectorizer.transform(email_list)

print vectorizer.vocabulary_.get("great") # return the location of the word "great" from the bag of words

#%%
import nltk
nltk.download()

#%%

from nltk.corpus import stopwords

sw = stopwords.words("english") 

#%%

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

stemmer.stem("responsiveness")

stemmer.stem("unresponsiveness")

#%% 

# TfIdf
# Tf - term frequency
# Idf - inverse document frequency 


