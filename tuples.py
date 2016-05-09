# -*- coding: utf-8 -*-
"""
Created on Sun May 01 20:24:49 2016

@author: Ricardo
"""

x = ('Glen', 'Sally', 'Joseph') #tuples ar immutable
#you can´t sort, append, reverse
print x[2]
print max(x)

t = tuple()
print dir(t)

d = {'a':10,'b':1,'c':22}
print d.items()

t = sorted(d.items()) # sort by key
print t

t.sort(reverse=True) # if we want to sort in value for example we need to create a new list and add those values
print t

#top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
lst = list()
for key, val in counts.items():
    lst.append( (val, key))

lst.sort(reverse=True)

for val, key in lst[:10] :
    print key, val
    
#shorter version
c = {'a':10, 'b':1, 'c':22}    
print sorted( [(v,k) for k,v in c.items()])