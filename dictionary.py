# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:29:59 2016

@author: Ricardo
"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print purse

literals= {'chuck':1, 'fred':42, 'jan':100}
print literals

counts = dict()
names = ['csev','cwen','zqien','cwen']
for name in names:
    counts[name] = counts.get(name,0) +1
print counts

for key in counts:
    print key, counts[key]

twoiteration = {'chuck':1, 'Fred':42, 'jan':100}
for aaa,bbb in twoiteration.items():
   print aaa,bbb
   
stuff = dict()
print stuff.get('candy',-1)
        