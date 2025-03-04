#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

bracket_map = {'(': ')', '{': '}', '[': ']'}
open_brackets = bracket_map.keys()
close_brackets = bracket_map.values()

def isBalanced(s):
    # Write your code here
    s_open = []  # Stack of visited brackets
    
    for bracket in s:
        if bracket in open_brackets:
            # Add bracket to stack
            s_open.append(bracket)
        elif bracket in close_brackets:
            # Pair open and closed bracket
            # check if stack has any open brackets
            if len(s_open) == 0:
                # No open brackets
                return "NO"
            
            # The top of the stack must contain a matching open bracket
            top_bracket = s_open.pop()
            
            if bracket_map.get(top_bracket) != bracket:
                # brackets did not match
                return "NO"
        else:
            raise Exception("INVALID CHAR " + bracket)
    
    if len(s_open) > 0:
        return "NO"
    
    return "YES"
            
    
    
    

if __name__ == '__main__':
    result = isBalanced("{[()]}")

    print(result + '\n')
