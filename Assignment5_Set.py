# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:58:14 2019

@author: shashikant.r
"""
# 1. Write a Python program to create a set.
My_set = {'Creating','set',2019,'computervision'}
type(My_set)

# set feed with duplicate value
My_set_duplicate = {10,'chandrayana2','southpole','moon','mission','moon'}

My_set_duplicate


#2. Write a Python program to create an intersection of sets.
 # Intersection '&': Takes only common elements from both sets
Set1 = {1,2,3,4}
Set2 = {3,4,5,6}

setIntersection = Set1 & Set2 
setIntersection


#3. Write a Python program to create a union of sets.
# Union '|' : combines both sets and will not take have duplicate value

Set_union = Set1 | Set2

Set_union

#4. Write a Python program to create set difference.

# Difference : Compares first and second and will take not macting values
# from first set to second set 

Set_difference = Set1 - Set2
Set_difference

#5. Write a Python program to create a symmetric
# Symmetric difference '^':compares both set and takes only not common values 
# from both set

Set_SymmDiff= Set1 ^ Set2

Set_SymmDiff







