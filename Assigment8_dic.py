# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:36:26 2019

@author: shashikant.r
"""
#1. Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

# Creating dictionary 
sample_dictionary = {0: 10, 1: 20}
#Adding new element
sample_dictionary[2] =30

sample_dictionary




# 3. Write a Python program to sum all the items in a dictionary.

print(sum(sample_dictionary.values()))


# 4. Write a Python program to remove a key from a dictionary. 
# creating dictionary
Dictionary = {'Name' : 'Rolls royce',
              'model' : 'Phantom',
              'Rate' : '7 cr',
              'year' : 2018}
Dictionary
#Removing one key - value  pair
del Dictionary['Name']
Dictionary
