import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(abs((arr[i]-arr[i-1])) for i in range(0,len(arr)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
