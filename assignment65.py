# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:38:51 2016

@author: Ricardo
"""

#Write code using find() and string slicing (see section 6.10) 
#to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
ini = text.find('0')
number = float(text[ini:])
print number, type(number)

