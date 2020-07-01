# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:14:04 2020

@author: akash
"""

# Week 2 Number extraction from text file
import re
sum = 0
lst =[]
f=open("assignment_data.txt", "r")
for line in f:
    data = re.findall('[0-9]+', line)
    if len(data)!=0:      
        for d in data:
            lst.append(d)
            sum+=int(d)
        
print(lst)
print("Total numbers: ",len(lst))
print("Sum: ",sum)
