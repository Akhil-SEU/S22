#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:12:33 2022

@author: akhiljonnalagadda
"""


####################################################
#1. If then
####################################################


## for commands spacing dicates the hierachy of when it occurs, show by the h
age = 20  #h1
if (age == 20): #h1
#remeber the : post a loop 
    print("almost") #h2
    
####################################################
#2. loops
####################################################


#think of the for loops as a chunk of code that repeats for n number of times. 
#ie clean a dish till all dishes are clean or repeat clean dish 25x 

#example of a for loop to run a set number of times
for x in range(0,5): 
    print("Loop works" )



#if you want to print a number you have to tell py that a number must be shown as a string
for x in range (0,3):
    print ('Loop execution %d'  % (x))

#you can print the numberic like this you need the {%d'  % } when you add the numeric to the string print
for x in range (0,3):
     print ((x))   
    
    
#with stings
cars = ["Cobra","Mustang","Corvette"]
for x in cars:
   print(x)

##nest a loop
for x in range (0,3):
    m = 1
    while m < 4: 
         print(x+1)
         m = m+1
   
#while loops are the to run as long as a condition is met 

y=1 #assign a value to your while loop variable. 
while y<= 5: 
    print(y)
    y = y +1 # add to our y to increase its value so the loop will run till it reaches 5
    #while loops must have some conition that is finite such that it ends. 
   
    
   
####################################################
#3. inputs
####################################################
n = 1
while n < 2:
    name = input('Enter your name, or type quit to exit ')
    if name == "quit":
        break #end
    age = input('Enter your age, or type quit to exit ')
    if age == "quit":
        break #end
    GPA = input('Enter your GPA, or type quit to exit ')
    if GPA == "quit":
        break #end
    coffee = input('How much is Coffee, or type quit to exit ')
    if coffee == "quit":
        break #end
    print("My name is "+ name + " and I am " + age + " years old."+ " My GPA is " + GPA 
          + "." + " My coffee cost $" + coffee + ".")
        


#added loop for story 

n = 1
while n < 2:
    name = input('Enter your name, or type quit to exit ')
    if name == "quit":
        break #end
    age = input('Enter your age, or type quit to exit ')
    if age == "quit":
        break #end
    GPA = input('Enter your GPA, or type quit to exit ')
    if GPA == "quit":
        break #end
    coffee = input('How much is Coffee, or type quit to exit ')
    if coffee == "quit":
        break #end
    print("My name is "+ name + " and I am " + age + " years old."+ " My GPA is " + GPA 
          + "." + " My coffee cost $" + coffee + ".")
    again = input("Repeat? Yes or No?")
    if again == "no":
        break end;


####################################################
#4. functions
####################################################
    
#defien functions   
def sum3(a, b, c):
   return a + b + c

def avrg(first, *rests):
    return (first + sum(rests)) / (1 + len(rests))
# Sample use, Putting values
print (avrg(1, 2))
print (avrg(1,2,3,4))