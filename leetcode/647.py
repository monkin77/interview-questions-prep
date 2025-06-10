from typing import *

class Solution:

    '''
    Time Complexity: O(n)
    '''
    def isPalindrome(self, s:str, memoized: Optional[dict] = None) -> bool:
        '''
        Given a string s, returns True if palindrome
        '''
        if len(s) < 2:
            return True

        if s in memoized:
            return memoized[s]

        return s[0] == s[-1] and self.isPalindrome(s[1:-1], memoized) # Recursive call without the edge elements

    '''
    Time Complexity: O(n^2)

    Let's find all palindromic substrings by looking for all possible palindromes with the middle element fixed.
    For each character in the string, we can expand outwards to find all palindromes centered at that character.
    This approach is more efficient than checking all substrings individually as it avoids redundant checks.
    '''
    def countSubstrings(self, s: str) -> int:
        wordLen = len(s)

        numSols = 0
        
        # Check for odd-length palindromes
        for center in range(wordLen):
            l, r = center, center
            while l >= 0 and r < wordLen and s[l] == s[r]:
                numSols += 1
                l -= 1
                r += 1
        
        # Check for even-length palindromes
        for center in range(wordLen - 1):
            l, r = center, center + 1
            while l >= 0 and r < wordLen and s[l] == s[r]:
                numSols += 1
                l -= 1
                r += 1
        return numSols

    '''
    Time Complexity: O(n^2) * O(n) = O(n^3)
    '''
    def countSubstringsMemo(self, s: str) -> int:
        wordLen = len(s)

        numSols = 0
        memoized = {}
        for subLen in range(1, wordLen+1,1):
            numPossiblePalindromes = wordLen - subLen + 1
            for offset in range(numPossiblePalindromes):
                l, r = offset, offset+subLen
                curSubstring = s[l:r]

                # Check if the current substring is a palindrome
                isPalindrome = self.isPalindrome(curSubstring, memoized)

                # Save solution in memoization dictionary
                memoized[curSubstring] = isPalindrome

                if isPalindrome:
                    numSols += 1
        
        return numSols

    def countSubstringsNaive(self, s: str) -> int:
        wordLen = len(s)

        numSols = 0
        for subLen in range(1, wordLen+1,1):
            numPossiblePalindromes = wordLen - subLen + 1
            for offset in range(numPossiblePalindromes):
                l, r = offset, offset+subLen
                if self.isPalindrome(s[l:r]):
                    numSols += 1
        
        return numSols
    

res = Solution()
input1 = "abc"
input2 = "aaa"

sol = res.countSubstrings(input1)

print("Solution: ", sol)