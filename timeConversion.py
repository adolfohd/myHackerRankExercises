import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #

    parts = s.split(":")
    if "AM" in parts[2]:
        if parts[0] == "12":
            parts[0] = "00"
        else:
            parts[0] = parts[0]
    elif int(parts[0])<12:
        parts[0]=str(int(parts[0])+12)
    parts[2] = re.findall(r'\d+', parts[2])[0]

    return(":".join(parts))
    



s = "12:00:43PM"
print(timeConversion(s))