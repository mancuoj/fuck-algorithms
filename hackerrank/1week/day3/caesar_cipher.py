#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    ans = ""
    for i in s:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            shift = 97 if "a" <= i <= "z" else 65
            ans += chr(shift + ((ord(i) - shift + k + 26) % 26))
        else:
            ans += i
    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
