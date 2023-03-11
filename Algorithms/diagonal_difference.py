# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal_a = 0
    diagonal_b = 0
    
    size = len(arr)
    j = size - 1
    
    for i in range(0, size):
        diagonal_a += arr[i][i]
        diagonal_b += arr[i][j]
        j -= 1

    diff = diagonal_a - diagonal_b
    if diff < 0:
        return diff * (-1)
    else:
        return diff
    


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
