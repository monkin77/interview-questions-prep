#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_pal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True

def palindromeIndex(s):
    # Write your code here
    strLen = len(s)
    
    l, r = 0, strLen - 1
        
    # Slide the string from left and right and validate if letters in extremeties are equal
    while l < r:
        print(f"l: {l}, r: {r}")
        if s[l] == s[r]:
            # Extremety letters are equal, move the pointers
            l += 1
            r -= 1
            continue
            
        # If the letters are not the same
        
        # check if there is a solution by removing the letter at index l (left)
        is_remove_left_pal = is_pal(s[l+1:r+1])
        if is_remove_left_pal:
            return l
        
        # check if there is a solution by removing the letter at index r (right)
        is_remove_right_pal = is_pal(s[l:r])
        if is_remove_right_pal:
            return r
            
        # If none of the above conditions are met, then there is no solution
        return -1
        
    
    # If there is no solution by removing 1 char, or if the original str is already a palindrome,
    # returns -1. Otherwise, returns index of the char to remove
    return -1
    
    

if __name__ == '__main__':
    result = palindromeIndex("aaab")

    print(str(result) + '\n')
