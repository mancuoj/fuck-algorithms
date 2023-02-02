#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def palindromeIndex(s):
    # Write your code here
    l, r = 0, len(s) - 1
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1

    if l >= r:
        return -1
    if is_palindrome(s[l:r]):
        return r
    if is_palindrome(s[l + 1 : r + 1]):
        return l
    return -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + "\n")

    fptr.close()
