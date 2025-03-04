#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    if len(grid) == 0:
         return "YES"

    # Write your code here
    num_rows = len(grid)
    
    # Sort each row alphabetically in asceding order
    for row_idx in range(num_rows):
        # Sort the row
        grid[row_idx] = sorted(grid[row_idx])
    
    # Iterate each column and check if they are also alphabetically ordered
    num_cols = len(grid[0])
    for col_idx in range(num_cols):
        # build col
        curr_col = []
        for row_idx in range(num_rows):
            curr_col.append(grid[row_idx][col_idx])
        
        for idx in range(len(curr_col)-1):
            if curr_col[idx] > curr_col[idx+1]:
                # Column is not sorted
                return "NO"
                
    return "YES"
    

if __name__ == '__main__':
        grid = ["abc", "hjk", "mpq", "rtv"]

        result = gridChallenge(grid)

        print(result + '\n')
