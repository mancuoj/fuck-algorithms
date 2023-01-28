#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    # Write your code here
    mid = len(matrix) // 2
    find_max = lambda m, x, y: max(m[x][y], m[x][~y], m[~x][y], m[~x][~y])
    return sum([find_max(matrix, x, y) for x in range(mid) for y in range(mid)])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + "\n")

    fptr.close()
