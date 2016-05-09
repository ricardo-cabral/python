# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:07:33 2016

@author: Ricardo
"""

#8.4 Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and 
#if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
#fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    tmpLine = line.rstrip().split()
    for splited in tmpLine:
        if splited not in lst:
            lst.append(splited)
lst.sort()
print lst
    