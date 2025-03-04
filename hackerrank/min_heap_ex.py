#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
from heapq import heapify, heappush, heappop

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    # sort the cookies by sweetness value
    min_heap = []
    heapify(min_heap)
    
    # Adding initial items to the heap
    for elem in A:
        heappush(min_heap, elem)
    
    min_sweetness = min_heap[0]
    num_iters = 0
    while min_sweetness < k and len(min_heap) >= 2:
        # Remove the 2 cookies to make a new one
        new_cookie = heappop(min_heap) + (heappop(min_heap) * 2)
        
        # insert new cookie
        # min heap insertion occurs in O(log n) time
        heappush(min_heap, new_cookie)
        
        min_sweetness = min_heap[0]
        num_iters += 1
        
    if min_sweetness >= k:
        return num_iters
    
    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
