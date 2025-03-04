from typing import *

"""
Longest Palindromic Substring
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DYNAMIC PROGRAMMING APPROACH
        """
        Recurrence Relation:
        - is_palindrome[i..j] = s[i] == s[j] and is_palindrome[i+1...j-1]

        Base cases:
        - is_palindrome[i..i] = True
        - is_palindrome[i..i+1] = True, if s[i] == s[j]

        Thus, we are building the palindromes starting at the center value and adding the left and right values
        """
        s_len = len(s)

        # is_palindrome[i][j] will be True if substring s[i..j] is a palindrome
        is_palindrome = [[False] * s_len for _ in range(s_len)]

        # All substrings of length 1 are palindromes
        for i in range(s_len):
            is_palindrome[i][i] = True

        # longest_start and max_length track the start index and length of the longest palindrome found so far
        longest_start = 0
        max_length = 1

        # Check for palindromes of length 2
        for i in range(s_len - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                longest_start = i
                max_length = 2

        # Check for palindromes of length 3 or more
        for current_length in range(3, s_len + 1):
            # Fix the starting index
            for i in range(s_len - current_length + 1):
                # Get the ending index
                j = i + current_length - 1

                # Check if substring s[i+1..j-1] is a palindrome AND the first and last characters match
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

                    if current_length > max_length:
                        max_length = current_length
                        longest_start = i

        return s[longest_start : longest_start + max_length]

    def longestPalindromeMiddle(self, s: str) -> str:
        """
        At each iteration, we will try to add a left and right character to a substring and see if it still is a palindrome
        Hence, there will be ~ len(s) / 2 iterations at most. And we will use memoization to store the biggest palindrome found until now 

        Recurrence Relation:
        
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res



res = Solution()

input1 = "ababd"
input2 = "abbc"

sol = res.longestPalindrome(input2)

print("Solution: ", sol)