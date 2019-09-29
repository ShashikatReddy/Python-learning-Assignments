# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 03:53:07 2019

@author: shashikant.r
"""
#1. Write a Python program to sum all the items in a list.
 # Use function : sum()  for find  sum of all elements in the list
list = [10,20,30,40,50]
print('summation of all elements in the list is' ,sum(list)) # 150

#2. Write a Python program to get the largest number from a list

print('largest element of the list is ',max(list))





#3. Write a Python program to remove duplicates from a list.

first_list = ['abc',12,34,'abc',12,100,12]

first_set = set(first_list)
print(first_set)

type(first_set) # output type is set


#.................
first_list = ['abc',12,34,'abc',12,100,12]

second_list = []
for i in first_list:
    if i not in  second_list:
        second_list.append(i)
      
print(second_list)    
    

# why not this

for i in first_list:
    second_list = []
    if i not in  second_list:
        second_list.append(i)
      
print(second_list) 


#4. Write a Python program to check a list is empty or not

Empty_list = []

print(Empty_list) # output : []
type(Empty_list) # output : list

# checking if length of Empty_list is 0 then print this is empty list
if len(Empty_list)== 0:
    print('This is empty list')





#6. Write a Python program to find the second smallest number in a list
#Creating list    
my_list = [10,45,563,2738,1652,4674,244984,98282,774986]

# sort : will arrange elements of list in accesending order
my_list.sort()

my_list
my_list[-2]


""" 5. Write a Python program to print a specified list after removing the 0th, 4th and 5th
elements.
Sample List : [‘A', ‘B', ‘C', ‘D', ‘E', ‘F']
Expected Output : [‘B', ‘C', ‘D]  """ 

Sample_List =['A', 'B','C','D','E','F']

Zeoth = Sample_List[0]
fourth = Sample_List[4]
Fifth = Sample_List[5]
Sample_List.remove(Zeoth) or  Sample_List.remove(fourth) or Sample_List.remove(Fifth)

print(Sample_List)





















