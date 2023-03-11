# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for num in ar:
        sum += num

    return num



if __name__ == '__main__':

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)