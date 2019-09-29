# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:32:39 2019

@author: shashikant.r
"""
#Assigment 2 
""" 1. Write a code to List out the difference between bitwise ‘AND’ and logical & operators """

""" Logical 'and' operator  is used to perform operation on  boolean values such as True/False.
If both variables are True then 'and' operator returns True .
If both or anyone variable is False then it returns False.
  """
# Code
cc= True 
dd= False
ff= True

ee= cc and dd
print("value of ee is ", ee)

if (cc and dd==False):
    print("output of condition is false")

if(True and False==True):
    print("output of condtion is true")
else:
    print("output of  is False")
    
if(True and False==True):
    print("output of condtion is true")
else:
    print("output of  is False")


if(True and True==True):
    print("output of condtion is true")
else:
    print("output of  is False")
  
""" Bitwise & operation : Computer converts anything you right into binary format
0 and 1.So if you give any number as input it will be converted to respective bit value
and it copies result if both has values """

#Code for bitwise
""" 
input AA=20 its binarry value is 00010100 
input BB=21 its binarry value is 00010111  21
                                 00010100 20 return
"""
AA=20
BB=21
cc= AA & BB

dd=34 #00100010
ee=35 #00100011
      #00100010 retuns 34
ff= dd&ee
print("value of ff is ", ff)

#.......................................................................
""" 2.Write a code to take input from user and perform  """
#a. Arithmetic operation 
""" input function reads and alway returns as string irrespective of datatype value you give 
So, below im converting string to integer datatype using int function """

A1 = int(input("Enter a number: "))
A2 = int(input("Enter a number: "))


print("Entered bvalue of A1 is", A1)
print("Entered value of A2 is", A2)

type(A1)

""" Arthematic operation """
addition= A1+A2
print("addition of A1 and A2 is",addition)

#Subtaction
sub=A1-A2
print("Sub  A1 and A2 is",sub)

#multiplication
Multi = A1*A2
print("multiplication of A1 and A2 is",Multi)

#Division 
Div = A1/A2
print("Division of A1 and A2 is",Div)

#Modulus 
modulus = A1%A2
print("Modulus of A1 and A2 is",modulus)

#Exponential
Exp = A1**A2
print("Exponential of A1 and A2 is",Exp)

""" Logical operation """#.........................................

# bool function retuns True whatever input and retuns flase if its empty
true = bool(input("Enter1boolean value"))
false = bool(input("Enter2boolean value"))
print("value of true is ",true)
print("value of true is ",false)

# eval() function:If you know the string will be either "True" or "False"
# only using it if you're sure of the contents of the string
# if you enter 1 it retun int  so on for other datatype input
true = eval(input("Enter1boolean value"))
false = eval(input("Enter2boolean value"))
print("value of true is ",true)
print("value of true is ",false)



#Checking datatype
type(true)
type(false)

ee= true and false
print("value of ee is ", ee)

if (true and false==False):
    print("output of condition is false")

if(true and false==True):
    print("output of condtion is true")
else:
    print("output of  is False")
    
if(true and false==True):
    print("output of condtion is true")
else:
    print("output of  is False")


if(true and true==True):
    print("output of condtion is true")
else:
    print("output of  is False")


""" or operator """
gg= true or false
print("value of ee is", gg)

if(true or false==True):
    print("output of condtion is true")
else:
    print("output of  is False")


if(false or false==True):
    print("output of condtion is true")
else:
    print("output of  is False")


""" not operator """ # Use to reverse the operand value

hh=not true
print("value of hh is", hh)


if(not false==true):
    print("output of condtion is True")
else:
    print("output of  is False")


if(not true==false):
    print("output of condtion is true")
else:
    print("output of  is False")


if(not true==true):
    print("output of condtion is true")
else:
    print("output of  is False")
#......................................................................



true = eval(input("Enter1boolean value"))
false = eval(input("Enter2boolean value"))
print("value of true is ",true)
print("value of true is ",false)






"""3. Write a program to understand the bitwise shift operation """

""" << """ # Left shift it movs bits left specified number of positions
# Left shift multiplies the value 

w=20<<1
print("value of w is",w) # w va;ue will be  40

x=20<<2
print("value of x is",x) # w value will be 80

y=20<<3
print("value of y is",y) ## w value will be 160

z=20<<4
print("value of z is",z) ## w value will be 320

# Right shift divides  the value 

aa=20>>1
print("value of aa is ",aa) # value of aa is 10

bb=20>>2
print("value of aa is ",bb) # value of aa is 5


""" 4. Write a program to Multiply element using bitwise shift operation (‘<<‘ or ‘>>’) """
# Left shif  multiplies the value by position value 
# 

V1= 20
# if position is 1 then v1 will doulbled
V1_mutiple=V1<<1

V1_2multiple=V1<<2  # If postion is 2 then it double v1 and later doubles the results

V1_3multiple=V1<<3  

#As the postion incresd vale will e doubled as on prevoius value




































