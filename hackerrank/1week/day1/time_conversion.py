#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    a, b, c = s.split(":")
    if s[-2] == "P":
        if int(a) == 12:
            return "12:" + b + ":" + c[:2]
        else:
            return str(int(a) + 12) + ":" + b + ":" + c[:2]
    else:
        if int(a) == 12:
            return "00:" + b + ":" + c[:2]
        else:
            return a + ":" + b + ":" + c[:2]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
