#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.metrics import accuracy_score
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

#%%%

# KNN
from sklearn.neighbors import KNeighborsClassifier

clf_knn = KNeighborsClassifier()

clf_knn = clf_knn.fit(features_train, labels_train)

pred_knn = clf_knn.predict(features_test)

accuracy_knn = accuracy_score(pred_knn, labels_test)

# ADAboost
from sklearn.ensemble import AdaBoostClassifier

clf_ada = AdaBoostClassifier()

clf_ada = clf_ada.fit(features_train, labels_train)

pred_ada = clf_ada.predict(features_test)

accuracy_ada = accuracy_score(pred_ada, labels_test)
 

# RandomForest 
from sklearn.ensemble import RandomForestClassifier

clf_rdf = RandomForestClassifier()
clf_rdf = clf_rdf.fit(features_train, labels_train)

pred_rdf = clf_rdf.predict(features_test)

accuracy_rdf = accuracy_score(pred_rdf, labels_test)


print "KNN model accuracy: ", accuracy_knn
print "AdaBoost accuracy: ", accuracy_ada
print "Random forest accuracy: ", accuracy_rdf

#%%%%
plt.figure(1)
try:
    prettyPicture(clf_knn, features_test, labels_test)
    # prettyPicture(clf_rdf, features_test, labels_test)
except NameError:
    pass


plt.figure(2)
try:
    prettyPicture(clf_ada, features_test, labels_test)
    # prettyPicture(clf_rdf, features_test, labels_test)
except NameError:
    pass

plt.figure(3)
try:
    prettyPicture(clf_rdf, features_test, labels_test)
    # prettyPicture(clf_rdf, features_test, labels_test)
except NameError:
    pass

