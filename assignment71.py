# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:59:39 2016

@author: Ricardo
"""

# Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    fmtline = line.strip().upper()
    print(fmtline)

fh.close()