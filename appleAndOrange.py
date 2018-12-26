
import math
import os
import random
import re
import sys



# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    for i in range(0,len(apples)):
        if (a + apples[i])>=s and (a + apples[i])<=t:
            appleCount += 1
    for i in range(0, len(oranges)):
        if (b + oranges[i])>= s and (b + oranges[i]<= t):
            orangeCount += 1 
    print(appleCount) 
    print(orangeCount)  


s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

print(countApplesAndOranges(s, t, a, b, apples, oranges))