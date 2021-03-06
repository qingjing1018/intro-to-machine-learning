#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


# Visualize the data 

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#%%
import numpy as np

# Return the largest salary
max_salary = np.max(zip(*data)[0])  

# Return the key with the largest salary (outlier)
for key in data_dict.keys():
    if data_dict[key]["salary"] == max_salary:
        print key
        
#%%

# Remove the outlier
data_dict.pop('TOTAL', 0)

# Reformat the cleaned data 
data = featureFormat(data_dict, features)

# Re-visualize the data 

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


#%%%%

# Two people made bonuses of at least 5 million dollars, and a salary 
# of over 1 million dollars.  What are the names associated with those points?

for key in data_dict.keys(): 
    if data_dict[key]['salary'] > 1e6 and       \
        data_dict[key]['salary'] != 'NaN' and   \
        data_dict[key]["bonus"] > 0.51e7 and    \
        data_dict[key]['bonus'] != 'NaN' : 
        print key, data_dict[key]['salary'], data_dict[key]["bonus"]
    
    
    
    
    
    
    