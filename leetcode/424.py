from typing import *

"""
Longest Repeating Substring With Replacement
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len() has O(1) time complexity since Python stores the length of data structures as part of their metadata.
        maxLen = 0

        l, r = 0, 0

        # Map character of the current substring to their frequency
        freqMap: Dict[str, int] = {}

        maxFreq: int = 0   # Stores the max frequency ever found

        for r, c in enumerate(s):
            # Update the frequency map
            freqMap[c] = freqMap.get(c, 0) + 1

            # Update the max frequency
            maxFreq = max(maxFreq, freqMap[c])

            currSubstringLen = r - l + 1
            if currSubstringLen - maxFreq > k:
                # If the current substring does not obey the condition, shift the left pointer
                # Update the freqMap to remove the left character
                freqMap[s[l]] = freqMap.get(s[l]) - 1

                l += 1
            else:
                # Current substring is valid, check if it is the largest
                maxLen = max(currSubstringLen, maxLen)

        return maxLen


res = Solution()

input1 = ("XYYX", 2)
input2 = ("AAABABB", 1)
input3 = ("ABBB", 2)
input4 = ("AABABBA", 1)
sol = res.characterReplacement(input4[0], input4[1])

print("Solution: ", sol)