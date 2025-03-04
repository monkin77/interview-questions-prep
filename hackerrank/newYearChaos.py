#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    q = [i-1 for i in q]  # set queue to start at 0
    bribes = 0
    
    for idx, sticker in enumerate(q):
        # Check if the current person has moved more than 2 positions forward.
        # 2 is the max since they can only bribe at most 2 persons
        if sticker - idx > 2:
            print("Too chaotic")
            return
            
        # Check if the current person was bribed by others
        # in interval [sticker-1, idx]
        # if a person has a higher sticker than the current in this interval,
        # that means there was a bribe since initially they were sorted in ascending order
        for k in q[max(sticker - 1, 0):idx]:
            if k > sticker:
                bribes += 1

    print(bribes)

        
        
    

if __name__ == '__main__':
    q = [2, 4, 3, 1]

    minimumBribes(q)
