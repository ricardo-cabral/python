# -*- coding: utf-8 -*-
"""
Created on Sun May 08 18:23:48 2016

@author: Ricardo
"""
#Handling The Data
#The basic outline of this problem is to read the file, 
#look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' and then 
#converting the extracted strings to integers and summing up the integers.
import re
#handle = open('regex_sum_42.txt')
handle = open('regex_sum_248536.txt')


numlist = list()

for line in handle:
    numbers = re.findall('[0-9]+', line)
    for tmp in numbers:
        numlist.append(int(tmp))

print sum(numlist)