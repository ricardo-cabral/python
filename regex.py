# -*- coding: utf-8 -*-
"""
Created on Thu May 05 20:16:47 2016

@author: Ricardo
"""
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >=0:
        print line
hand.close()

#regular expressions
hand1 = open('mbox-short.txt')
for line in hand1:
    line = line.rstrip()        
    if re.search('^X.*', line): #^match the start of the line, dot matches any character, * represents any number of times
        print line
hand1.close        

hand2 = open('mbox-short.txt')
for line in hand2:
    line = line.rstrip()        
    if re.search('^X-\S+:', line): # ^ start of the line, \S any non-whitespace character, + one or more times
        print line
hand2.close        

hand3 = open('mbox-short.txt')
for line in hand3:
    line = line.rstrip()        
    if re.findall('[0-9]+', line):#one or more digits, find all find all the situations that my string matches
        print line
hand2.close        