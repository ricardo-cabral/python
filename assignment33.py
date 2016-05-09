# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:32:04 2016

@author: Ricardo
"""

#Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:

#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.
try:
    score = raw_input("Enter Score: ")

    finalScore = float(score)

    if(finalScore < 0.0 or finalScore > 1.0):
        print('Error: Score out of range')

    if(finalScore < 0.6):
        print('F')
    elif (finalScore >= 0.6 and finalScore < 0.7):
        print('D')
    elif(finalScore >= 0.7 and finalScore < 0.8):
        print('C')
    elif (finalScore >= 0.8 and finalScore < 0.9):
        print('B')
    elif (finalScore >= 0.9 and finalScore <=1.0):
        print('A')
except:
    print('Error parsing score')