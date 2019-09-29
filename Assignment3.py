# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:49:43 2019

@author: shashikant.r
"""
#1. Write a program to see how single condition and multiple condition based statement works.
#(hint: single condition based if-else)

# Single condition
a = 30
b = 50
if a>b:
    print('a is greater than b', a)
else:
    print('b is greater than a:',b)

#Multiple condition 
CC = 23
DD =3
EE= 67
if CC >DD:
    print('CC is greater than DD')
    if CC>EE:
        print("CC is greatest than DD and EE")
    else:
        print ("EE is greater than DD and CC")
elif CC>EE:
        print('CC is greater than EE and DD')
        print('Gretest value ', CC)
else:
   print('EE is greater than CC and DD')
   print('Gretest value ', EE)
   
  # Multiple condition  
C = 34
D = 10
E=  1234        

if (C>D):
      print('C is greater than D')
      if(C>E):
          print('C is greatest among all')
      else:
        print('E is reatest among all')
        
elif C== D == E:
    print('C,D and E are equal')
    
else:
    print('D is greateer tan C')
    if(D>E):
        print('D is greatest among all')
    else:
        print('E is greatest among all')
           
   
#2. Write a program to differentiate between for loop and while loop 
""" A for loop is used for iterating over a sequence (that is either a
 list, a tuple, a dictionary, a set, or a string).     
 
With the for loop we can execute a set of statements, once for each item
 in a list, tuple, set etc. """
fruits = ['apple','banana','cherry']

for i in fruits:
    print( i)


# Break : Stops loop when condition is satisfied 
for i in fruits:
    if i == 'banana':
        break
    print(i)


# looping through a string
Adhiyogi = 'Om nama shivaya'
for i in Adhiyogi:
    print(i)


""" for loop iteration on Dictionary """

dictionary = {'apple' : '200 rupee',
              'banana' : '80 rupee',
              'cherry' : '400 ruppe',
              'pomagranate' : '180 rupee',
              'American orange' : '250 ruppe'}


# both key and values are printed
for key, value in dictionary.items():
   print(key,value)
   
# only key are printed
for i in dictionary:
    print(i)
    
# Break : stops loop when i== 180 rupee

for i in dictionary:
    if dictionary[i] == '180 rupee':
         break
    print(dictionary[i])


#Exit the loop when i is "180 rupee": value of  i value will printed and break executed later
for i in dictionary:
   print(i)
   if dictionary[i] == '180 rupee':
    break
  
    
    
 # Both key and value are printed
d = {'x': 1, 'y': 2, 'z': 3} 
for key in d:
    print( key, 'corresponds to', d[key])

# only value are prited 
d = {'x': 1, 'y': 2, 'z': 3} 
for key in d:
    print( d[key])

""" Continue statement  : With the contiinue statement we can stop the
 current iteration of the loop , and continue with the next: """
 
dictionary = {'apple' : '200 rupee',
              'banana' : '80 rupee',
              'cherry' : '400 ruppe',
              'pomagranate' : '180 rupee',
              'American orange' : '250 ruppe'}
 
 
for i in dictionary:
    if dictionary[i] == '180 rupee':
         continue
    print(dictionary[i])
   
   
   
 
""" while loop:
With the while loop we can execute a set of statements as long as a condition is true. """

# Here we are initially assinging x  as 1 and given while loop condition
# Note : We need to increment by some value other wise the loop will never end 
#with same inirail value


x = 1
while x<6:
    print('value of  x is',x)
    x += 1


y = 0.5
while y<6:
    print('value of  y is',y)
    y += 1


#3. Write a program to see how break, continue and pass works
    
""" With the break statement we can stop the loop before it has looped
 through all the items:  """
 
# list:
fruits = ['apple','banana','cherry']

for i in fruits:
    if i == 'banana':
        break
    print(i)
#dictionary:
 
dictionary = {'apple' : '200 rupee',
              'banana' : '80 rupee',
              'cherry' : '400 ruppe',
              'pomagranate' : '180 rupee',
              'American orange' : '250 ruppe'}
     

for i in dictionary:
    if dictionary[i] == '180 rupee':
         break
    print(dictionary[i])    
    

""" Continue statement  : With the contiinue statement we can stop the
 current iteration of the loop , and continue with the next: """
 # Continue skips current iteration and moves to next
 # list:
fruits = ['apple','banana','cherry']

for i in fruits:
    if i == 'banana':
        continue
    print(i)


# Dictionary
 
dictionary = {'apple' : '200 rupee',
              'banana' : '80 rupee',
              'cherry' : '400 ruppe',
              'pomagranate' : '180 rupee',
              'American orange' : '250 ruppe'}
 
 
for i in dictionary:
    if dictionary[i] == '180 rupee':
         continue
    print(dictionary[i])


""" Pass statement : Does nothing when a condition is satisfied """
#list
fruits = ['apple','banana','cherry']

for i in fruits:
    if i == 'banana':
        pass
    print(i)


# Dictionary
 
dictionary = {'apple' : '200 rupee',
              'banana' : '80 rupee',
              'cherry' : '400 ruppe',
              'pomagranate' : '180 rupee',
              'American orange' : '250 ruppe'}
 
 
for i in dictionary:
    if dictionary[i] == '180 rupee':
         pass
    print(dictionary[i])
