import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if(n==1):
        return 1
    prod=n*extraLongFactorials(n-1)
    return prod

print(extraLongFactorials(100))