#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from operator import sub
    import numpy as np
    
    difference = np.absolute(map(sub, predictions, net_worths))   
    
    # Return the indices of the top 90% smallest errors 
    # a.k.a. exclude the 10% largest errors 
    
    idx = np.argpartition(difference, len(difference)*9/10, axis = 0)[:len(difference)*9/10]     
  
    cleaned_data = zip(ages[idx], net_worths[idx], difference[idx])

    return cleaned_data

