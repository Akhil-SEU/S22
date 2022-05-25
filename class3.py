#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:33:21 2022

@author: akhiljonnalagadda
"""

#################################################
#1. How to use base functions
#################################################

#use adders
a = "hi"
b = a.upper()
print(a)
print(b)

#length of string
len(a)

#round
round(5/4)

#min/max
min(1,2,4)
max(1,2,4)

#sort
ls = [1,2,3,4]
sorted(ls)
print(ls)

#total
total = sum(ls)
print(total)


#replace
rep = "The phrase is cool"
rep.replace('cool', 'lame')
print(rep)

#split
split = 'Hello World'
split.split(' ')

#append
dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]
dog.append("aj")
print(dog)



#################################################
#2. Dictionaries
#################################################

#use a dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict.get("model")
print(x)




dog_dict = {'name': 'Freddie',
'age': 9,
'is_vaccinated': True,
'height': 1.1,
'birth_year': 2001,
'belongings': ['bone', 'little ball']}

#return key
dog_dict.keys()

#use it
dog_dict['name'] 
dog_dict['height'] 




#################################################
#3. date times- lot fo work here. Just keep googling it
#################################################
##these are packages 
import time
from datetime import date 
from datetime import datetime


today = date.today() ##pull date
birthday = date(today.year, 6, 24) #use date format
my_birthday = date(1998, 7, 4)

#add a year
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
    
#use it as and int
time_to_birthday = abs(my_birthday - today)
print(my_birthday.month)

    
    
#format dates

date_format = '%d-%m-%Y'
date_string= '01-04-2022'
mydate = datetime.strptime(date_string, date_format)
print(mydate)
print(mydate.month)
print(mydate.day)
 print(mydate.year)   
    
 
    
 #################################################
 #4. log loop
 #################################################
#log books

test_dictionary = {}
x = 1
while x<10:  
    key = str(input('Add key? Yes or No '))
    if key == "no" or key == "NO" or key == "No":
        break
    new_key = input('Enter new key: ')
    new_age = input('Enter new age: ')
    test_dictionary [new_key] = new_age
    x= x+1
print(test_dictionary )   
    
    
#################################################
#4. csv
#################################################

import csv  

with open('baby-names.csv', newline='') as csvfile:
   names_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
   for row in names_file:
       print(', '.join(row))    
      

import pandas as pd
df = pd.read_csv ('baby-names.csv')
      
df_mean = df["percent"].mean()
print(df_mean)
      
df_mean2 = df.iloc[:, 2].mean()
print(df_mean2)