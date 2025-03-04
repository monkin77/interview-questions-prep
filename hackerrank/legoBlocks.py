#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    MOD = 10**9 + 7
    
    # Step 1) Calculate possible combinations for a single row
    # total combinations for a wall of height 1
    total_combs_row = [0 for _ in range(m+1)]
    
    # Define base cases
    if m >= 1:
        total_combs_row[1] = 1
    if m >= 2:
        total_combs_row[2] = 2
    if m >= 3:
        total_combs_row[3] = 4
    if m >= 4:
        total_combs_row[4] = 8
    
    for i in range(5, m+1):
        # If width is at least 4, we can place any type of lego, therefore
        # total solutions = sum of solutions by placing each type of lego
        total_combs_row[i] = (total_combs_row[i-1] + total_combs_row[i-2] + 
            total_combs_row[i-3] + total_combs_row[i-4]) % MOD
    
    # Step 2) Define the total number of combinations for a wall of height n
    total_combs = [(combs_num**n) % MOD for combs_num in total_combs_row]
    
    # Step 3) Find the valid combinations. For this, the Total num. of layouts
    # must be subtracetd by the invalid combinations.
    # Invalid combinations have a breakpoint/split in the middle, which is 
    # what we are forcing with split_pos
    solid = [0 for _ in range(m+1)]
    # Define base cases
    solid[1] = 1
    for solid_width in range(2, m+1):
        invalid_combs = 0
        for split_pos in range(1, solid_width):
            invalid_combs += ((solid[split_pos] * total_combs[solid_width-split_pos]) % MOD)
        
        solid[solid_width] = (total_combs[solid_width] - invalid_combs) % MOD
    
    return solid[-1]
    


if __name__ == '__main__':
    n, m = 2, 2

    # result = legoBlocks(n, m)

    result = totalCombs(4, 7)

    print(str(result) + '\n')
