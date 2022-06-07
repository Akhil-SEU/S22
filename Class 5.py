#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 08:45:29 2022

@author: akhiljonnalagadda
"""

import pandas as pd

import numpy as np

import scipy as sp

 ##################################
 #1 Sd
 #######

d = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,92,99,69],
   'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
df = pd.DataFrame(d)
answer= df.std()
print("The standard deviations of the 3 columns are:")
print (answer)







################################################
#2. corr
#############

d = {  'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,92,99,69],
   'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
df = pd.DataFrame(d)
print(df.corr())
          

################################################
#3. by array
#############





values = {"X":[20, 25, 30, 35, 40, 45],

          "Y":[10, 9, 9, 8, 8, 7]};


dataFrame       = pd.DataFrame(data=values);
df = dataFrame 

print("DataFrame:");

print(dataFrame);

 

corrrelation    = dataFrame.corr(method="pearson");

print("Pearson correlation coefficient:");

print(corrrelation);

 

corrrelation    = dataFrame.corr(method="kendall");

print("Kendall Tau correlation coefficient:");

print(corrrelation);

 

corrrelation    = dataFrame.corr(method="spearman");

print("Spearman rank correlation:");

print(corrrelation);

################################################
#4. cov.
#############
df.cov()