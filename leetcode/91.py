from typing import *

'''
Decode Ways

A string consisting of uppercase english characters can be encoded to a number using the following mapping:

To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.
'''
class Solution:
    def __init__(self):
        # Memoize the nº of solutions for substrings
        self.saved_sols = {}

    def numDecodings(self, s: str) -> int:
        # Base cases
        if len(s) == 0:
            return 1
        if len(s) == 1:
            # Valid solution if char is between 1 and 9
            return int("1" <= s <= "9")
        
        # Check if the current substring has been computed before
        if s in self.saved_sols:
            return self.saved_sols[s]

        if len(s) == 2:
            # Has solution with length 2 if encoded messsage is between 
            # 1 and 26 -- valid chars 
            two_char_sol = int("1" <= s <= "26")
            
            # See if there is also a solution choosing 1 char at a time
            one_char_sol = 0
            # First check if first char is valid
            if "1" <= s[0] <= "9":
                one_char_sol = self.numDecodings(s[1:])

            # Sum the solutions for both cases
            all_sols = two_char_sol + one_char_sol

            # Store the result in the memoization dictionary
            self.saved_sols[s] = all_sols

            return all_sols

        # Recursive Formulation
        one_digit = s[0]
        two_digit = s[:2]

        # Check solutions taking only one digit
        num_take_one_digit_sols = 0
        if "1" <= one_digit <= "9":
            # If the selected digit is valid
            num_take_one_digit_sols += self.numDecodings(s[1:])

        # Check solutions taking two digits
        num_take_two_digit_sols = 0
        if "1" <= two_digit <= "26":
            # If the selected digits are valid
            num_take_two_digit_sols += self.numDecodings(s[2:])

        # Sum the nº of solutions for each recursive scenario
        all_sols = num_take_one_digit_sols + num_take_two_digit_sols

        # Store the result in the memoization dictionary
        self.saved_sols[s] = all_sols

        return all_sols
        
