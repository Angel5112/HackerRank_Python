# Reverse an array of integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    new_array = []

    for i in range(len(a) - 1, -1, -1):
        new_array.append(a[i])

    return new_array



if __name__ == '__main__':

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)

    print(res)