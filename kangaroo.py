
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        vf = v1 # velocity of fastest
        xf = x1
        vs = v2 # velocity of slowest
        xs = x2
    else :
        vf = v2
        xf = x2
        vs = v1
        xs = x1

    while xs >= xf :
        if xs == xf :
            return("YES")
        else :
            xs += vs
            xf += vf
    return("NO")

print(kangaroo(0, 2, 5, 3))