# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:35:03 2019

@author: shashikant.r
"""

# 1. Write a Python program to calculate the length of a string.

LengthString = 'Convolution neural network'

print(len(LengthString)) #26

# 5. Write a Python program to check whether a string starts with specified characters.

print(LengthString.startswith('C')) # True

print(LengthString.startswith('c')) # False , beacuse its case sensithive 

print(LengthString.startswith('T')) #False , Becuase string start with 'C'


# 4. Write a Python program to remove the characters which have odd index values of a given string.

string = 'Homogeneous'


         
string = 'Homogeneous'
for i in string:
    x=string.find('i')
    if x%2!=0:
        print(string[x])
        
string = 'Homogeneous'        
for i in string:
    x=string.index("i")
    if x%2!=0:
        print(string[x])
        
string = 'Homogeneous'  
      
for i in string:
    print(string.find('i'))
      
        

        
        
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
      
    # checking condition 
    if num % 2 != 0: 
       print(num, end = " ") 

# 2. Write a Python program to count the number of characters (character frequency) in a string

Sample_string = 'google.com'
print('g:',string.count('g'), 'o:',string.count('o'), 'l:',string.count('l'), 'e:',string.count('e'), 'c:',string.count('c'),'m:',string.count('m'))


















