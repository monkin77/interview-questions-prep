from typing import *
import math

"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        lCurr = 0
        rCurr = 0

        charIdxMap: Dict[str, int] = {}

        for idx, char in enumerate(s):
            rCurr = idx     # New character for the substring

            # Repeated char means we skip the substring until the previous occurence of the character disappears
            if char in charIdxMap:
                newLCurr = charIdxMap[char] + 1
                lCurr = max(newLCurr, lCurr)
            
            # Add the char to the map
            charIdxMap[char] = idx

            # Check if the new substring is the largest one yet
            currLen = rCurr - lCurr + 1
            if currLen > maxLen:
                maxLen = currLen
        
        return maxLen
                
            
res = Solution()

input1 = "zxyzxyz"
input2 = "xxxx"
input3 = "abba"
sol = res.lengthOfLongestSubstring(input3)
print("Solution: ", sol)