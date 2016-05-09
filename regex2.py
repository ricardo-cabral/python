# -*- coding: utf-8 -*-
"""
Created on Fri May 06 19:26:56 2016

@author: Ricardo
"""

import re

#regular expressions
hand = open('mbox-short.txt')
for line in hand:
    y = re.findall('^From (\S+@\S+)', line) #at least one non-whitespace character containing @ and return what is inside the parentheses
    if y:
        print y
hand.close   

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
result = re.findall('^From (\S+@\S+)', data)
print result

atpos = data.find('@')
#print atpos #21

sppos = data.find(' ', atpos)
#print sppos #31

host = data[atpos+1:sppos]
print host

words = data.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

w = re.findall('^From .*@([^ ]*)',data) #[^ ]Match non-blamk character, * match many of them
print w

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0=9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)

print 'Maximum: ', max(numlist)

dollar = 'We just received  $10.00 for cookies'
res = re.findall('\$[0-9]+', dollar)
print res

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y

again = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pl = re.findall('\S+?@\S+', again)
print pl
