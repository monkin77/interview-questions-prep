#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    # Tower heights
    heights = [m] * n
    
    # all towers have the same initial height, so we can calculate how many moves can be done at 1 tower
    # and then multiply by the number of tower
    h1 = heights[0]
    
    # Track number of oper
    num_tower_oper = 0
    while h1 != 1:
        num_tower_oper += 1
        
        # Find the minimum divisor of curr_height (Except 1)
        min_div = -1
        for divisor in range(2, int(h1//2 + 1), 1):
            if h1 % divisor == 0:
                # Found the min divisor
                min_div = divisor
        
        # If min_div is -1, means that it is a prime number (we can only reduce its height to 1)
        if min_div == -1:
            # Reduce height to 1
            h1 = 1
        else:
            # Calculate the max_div
            max_div = h1 / min_div
            
            # Set the height to max_div
            h1 = max_div
    
    # Total number of opers
    total_opers = num_tower_oper * n
    
    print(f"total_opers: {total_opers}")
    
    # if the total number of opers is even -> P2 wins
    if total_opers % 2 == 0:
        return 2
    return 1
    
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(str(result) + '\n')
