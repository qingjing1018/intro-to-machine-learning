#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# introduce partial training set using 1% of the full data set 
features_train_p = features_train[:len(features_train)/100] 
labels_train_p = labels_train[:len(labels_train)/100]


#%%
#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel = 'linear')  # specify to use linear kernel or it takes too long

t0 = time()

clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"

t1 = time()

pred = clf.predict(features_test)

print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)

print accuracy

#########################################################

#%%

t0 = time()

clf.fit(features_train_p, labels_train_p)

print "training time:", round(time()-t0, 3), "s"

t1 = time()

pred = clf.predict(features_test)

print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)

print "model accuracy is :", accuracy 

#%%%%
# change kernel to rbf and compare accuracy and time
clf = SVC(kernel = 'rbf')

t0 = time()
clf.fit(features_train_p, labels_train_p)

print "training time:", round(time()-t0, 3), "s"

t1 = time()

pred = clf.predict(features_test)

print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)

print "model accuracy is :", accuracy 


#%%%%
# Change C parameter value to compare accuracy

c_value = [10.0, 100.0, 1000.0, 10000.0]

for c in c_value:
    clf = SVC(C = c, kernel = 'rbf')
    t0 = time()
    clf.fit(features_train_p, labels_train_p)
    
    print "C = ", c
    print "training time :", round(time()-t0, 3), "s"

    t1 = time()

    pred = clf.predict(features_test)

    print "prediction time:", round(time()-t1, 3), "s"

    accuracy = accuracy_score(pred, labels_test)

    print "model accuracy is :", accuracy 

#%%%%
# C = 10000 gives the best training accuracy 
# Use the full training set to train rbf model with C = 10000

c = 10000.0

clf = SVC(C = c, kernel = 'rbf')
t0 = time()
clf.fit(features_train, labels_train)
    
print "C = ", c
print "training time :", round(time()-t0, 3), "s"

t1 = time()

pred = clf.predict(features_test)

print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)

print "model accuracy is :", accuracy 

#%%%%
# Extracting predictions from an SVM
# Using 1% of the training data 

c = 10000.0
clf = SVC(C = c, kernel = 'rbf')

clf.fit(features_train_p, labels_train_p)

pred = clf.predict(features_test)

idx = [10, 26, 50]

for num in idx: 
    ans = pred[num] 
    if ans == 1:
        author = "Chris"
    elif ans == 0: 
        author = "Sara" 
    print "The %s th email is from %s" %(str(num), author)     
        
#%%%%%
# Find the number of emails that are predicted to be in the "Chris" class (labeled as 1)
# Use full training set
# Method: sum all predictions (Chris = 1, Sara = 0)

features_train, features_test, labels_train, labels_test = preprocess()

c = 10000.0
clf = SVC(C = c, kernel = 'rbf')

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

pred_chris = sum(pred)
print pred_chris








