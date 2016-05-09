# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:48:13 2016

@author: Ricardo
"""

#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent 
#the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines 
#as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address 
#to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary 
#using a maximum loop to find the most prolific committer.
#expected cwen@iupui.edu 5
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if(line.rstrip().startswith("From:")):
        splited = line.split()
        counts[splited[1]] = counts.get(splited[1],0) +1        

email = None
greatest = None
for key in counts:
    if(counts[key] > greatest):
        email = key
        greatest = counts[key]

print email, greatest
    
        