#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#%%%
# Number of data points (keys) in the data set 
print len(enron_data)

# Number of features 
print len(enron_data["SKILLING JEFFREY K"])

# Number of POI in the dataset 
poi_num = 0

for key in enron_data.keys():
    if enron_data[key]["poi"] == 1:
        poi_num += 1

print poi_num
        
#%%%%

# Like any dict of dicts, individual people/features can be accessed like so:
# enron_data["LASTNAME FIRSTNAME"]["feature_name"] 
# or
# enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]       
        
# What is the total value of the stock belonging to James Prentice?
print enron_data["PRENTICE JAMES"]["total_stock_value"]   

# How many email messages do we have from Wesley Colwell to persons of interest?    
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What’s the value of stock options exercised by Jeffrey K Skilling?

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money 
# (largest value of “total_payments” feature)?

print "Skilling: ", enron_data["SKILLING JEFFREY K"]['total_payments']
print "Fastow: ", enron_data["FASTOW ANDREW S"]['total_payments']
print "Lay: ", enron_data["LAY KENNETH L"]['total_payments']

#%%%%
num_salary = 0 
num_email = 0 

for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        num_salary += 1
    if enron_data[key]['email_address'] != 'NaN':
        num_email += 1

print num_salary, num_email

#%%%%

# How many people in the E+F dataset (as it currently exists) have “NaN” for their 
# total payments? What percentage of people in the dataset as a whole is this?

num_nan_payment = 0

for key in enron_data.keys():
    
    if enron_data[key]['total_payments'] == 'NaN':
        num_nan_payment += 1

percentage_of_total = "{:.0%}".format(float(num_nan_payment)/ len(enron_data))

print "Number of people who have NaN as totoal payment: ", num_nan_payment

print "% of total: ", percentage_of_total

#%%%%

# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?

num_nan_poi = 0 

for key in enron_data.keys():   
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]["poi"] == 1:
        num_nan_poi += 1

percentage_of_poi = "{:.0%}".format(float(num_nan_poi)/ poi_num)
print "% of POI: ", percentage_of_poi










