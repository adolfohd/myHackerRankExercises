import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_height = 0
    candles = 0
    for i in range(0, len(ar)):
        if ar[i]>max_height :
            max_height = ar[i]
            candles = 1
        elif ar[i]==max_height:
            candles += 1
    return(candles)


ar = []
ar.append(1)
ar.append(1)
ar.append(1)
ar.append(2)
ar.append(0)

print(birthdayCakeCandles(ar))