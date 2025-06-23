from typing import *
from unittest import TestResult

"""
Minimum Window Substring
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Time Complexity: O(s * num_diff_chars)
        '''
        l, r = 0, 0
        if len(s) < len(t) or len(s) == 0 or len(t) == 0:
            # s must be >= t and both non-empty
            return ""

        target_char_counts = {}
        # build target char counts
        for char in t:
            target_char_counts[char] = target_char_counts.get(char, 0) + 1

        # Dict of char counts from the current substring window which belong to t
        cur_char_counts =  {}
        per_char_index = {} # map containing the index positions of each char ordered by their occurrence. Each value is a list of indices

        # Store the min found substring
        min_str = ""

        # Store the current nº of relevants chars
        num_chars = 0
        num_target_chars = sum(target_char_counts.values())

        # Slide window through s with left and right pointers
        while r < len(s):
            # new char -> c
            c = s[r]
            
            # Check if current char is in t
            if c in target_char_counts.keys():
                # c is a relevant character

                # Add the current char count
                cur_char_counts[c] = cur_char_counts.get(c, 0) + 1
                # Add the index to the per_char_index map
                per_char_index[c] = per_char_index.get(c, []) + [r]

                if num_chars == 0:
                    l = r
                
                num_chars += 1

                # Remove extra occurences of the character -> There is at most 1 extra element because we are adding 1 character at a time
                if cur_char_counts[c] > target_char_counts.get(c, 0):
                    # Get the index of the leftmost occurence of this char
                    rem_idx = per_char_index[c][0]
                    per_char_index[c].pop(0)
                    
                    # Check if the left pointer changes
                    if rem_idx == l:
                        l = r
                        for idx_arr in per_char_index.values():
                            if len(idx_arr) > 0:
                                l = min(l, idx_arr[0])

                    # Update the cur_char_count to the exact nº of chars we need
                    cur_char_counts[c] -= 1
                    num_chars -= 1

                # Check if we currently have all the chars from t
                if num_chars == num_target_chars:
                    cur_str_len = r - l + 1
                    if cur_str_len < len(min_str) or len(min_str) == 0:
                        # Update the min string
                        min_str = s[l:r+1]   
            else:
                pass
                
            r += 1
        
        return min_str



res = Solution()

input1 = ("OUZODYXAZV", "XYZ")
input2 = ("xyz", "xyz")
input3 = ("a", "a")
input4 = ("ab", "b")
input5 = ("cabwefgewcwaefgcf", "cae")
input6 = ("ADOBECODEBANC", "ABC")

sol = res.minWindow(input6[0], input6[1])

print("Solution: ", sol)