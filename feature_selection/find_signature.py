#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

accuracy  = accuracy_score(pred, labels_test)

print 'Accuracy:', accuracy
print clf.score(features_test, labels_test)

importance = clf.feature_importances_

print 'Maximum importance:', max(importance)

index_max = np.argmax(importance)
print 'Maximum value index:', index_max

top_features = [(number, feature, vectorizer.get_feature_names()[number]) for number, feature in zip(range(len(clf.feature_importances_)), clf.feature_importances_) if feature > 0.2]






