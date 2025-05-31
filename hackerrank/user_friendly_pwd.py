#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
MOD = (10**9) + 7
p = 131

def hashPwd(rawPwd) -> int:
    str_len = len(rawPwd)
    acc = 0
    
    for i, c in enumerate(rawPwd):
        multiplier = p**(str_len-1-i)
        asciiVal = ord(c)
        
        acc = (acc + (asciiVal * multiplier)) % MOD
    
    return acc
    
# def decodePwd(hashedPwd):
#     res = ""
    
#     cur_hash = hashedPwd
#     while cur_hash > 0:
#         char_ascii_val = cur_hash % 131
        
#         char = chr(char_ascii_val)
def similarPwd(tryPwd, realPwd):
    '''
    Check if tryPwd is the same as realPwd or the same with 1 more char appended to it
    '''
    if tryPwd == realPwd:
        return True
    
    # check if they are similar, with 1 more char appended
    
    # if that is the case, we need to shift the realPwd to the left, as we have a new character on tryPwd
    # to the right
    shiftedPwd = (realPwd * p) % MOD
    
    # Then, the last character can be any ASCII letter or digit
    # Set the min and max vals for shiftedPwd
    min_ascii_val = ord('0')
    max_ascii_val = ord('z')
    # set vals
    min_shifted_pwd = shiftedPwd + min_ascii_val
    max_shifted_pwd = shiftedPwd + max_ascii_val
    
    # Returns true if the distance between the triedPwd and shiftedPwd
    # is less than max_dist
    return min_shifted_pwd <= tryPwd <= max_shifted_pwd
        

def authEvents(events):
    # Shape of events: list[event] - event: (event_type, event_param)
    # returns: list[int] -> success (1) or failure(0) of each authorization attempt
    # Write your code here
    
    res_status = []
    
    cur_password = None # Stores the current hashable password at any time step (1st event must be a set password event)
    for event in events:
        event_type, param = event
        if event_type == "setPassword":
            cur_password = hashPwd(param)
        
        elif event_type == "authorize":
            if similarPwd(int(param), cur_password):
                res_status.append(1)
            else:
                res_status.append(0)
        else:
            raise Exception("Unknown event type: " + event_type)
    
    return res_status
    

if __name__ == '__main__':
    events = [
        ['setPassword', 'HnKYaX'],
        ['authorize', '776923238'],
        ['setPassword', 'f'],
        ['authorize', '84'],
        ['setPassword', 'wwmq6O'],
        ['authorize', '251714951']
    ]
    result = authEvents(events)

    print('\n'.join(map(str, result)))
    print('\n')