# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:04:01 2022

@author: clcas
"""



##########################
#example of list add
#use a list to store more values then one, currently you overwrite the variable
###########
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
########




##########################
#1. function of average
###########
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg



##########################
#2. set up blank lists and loop
###########
n = 1
name_list = []
age_list = []


##########################
#3. game
###########
while n < 2:

      Name = str(input('Type to your friends name ')) #Make sure its a string input
      if Name == 'Name':
         break #end
      name_list.append(Name) #add to list
      age = int(input('Enter their age ')) ##needs to be an int
      if age == "No" or age == "no": #upper/lower options
          break
      age_list.append(age) #add age
      avg_age = cal_average(age_list) #get avg, this value will be reaasigend every loop
      again = input("Add another friend? Yes or No? ") 
      if again == "No" or again  == "no":
          List = input('Would you like a list of your friends and their average age?, Yes or type No ')
          if List == "Yes" or List== "yes":  
              names_out = ','.join(name_list) #make it a string to print, other ways to do it too!
              age_out = str(avg_age) #personally i like making ints string before the print or you can do as we did in class!
              print("Your friends are "+ names_out + ", and their average age is " + age_out + " years old.")
              break #end;
          if List == "No" or List== "no": 
              break #end;