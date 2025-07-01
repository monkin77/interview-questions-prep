from typing import *

class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {} # dict of {char: Trie}
        self.isEndOfWord = False

"""
Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
"""
class Solution:
    def __init__(self):
        # Stores target substrings "s" which are not possible to build
        self.memo: set = set()  # Store solutions

    '''
    n <- length of s
    m <- Nº words in wordDict
    t <- Max length of word in wordDict

    Time Complexity: O(n * t^2 + m*t)
    Space Complexity: O(n + m*t)
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Define the Trie containing the words in the dict
        self.root = Trie()  # Root node of the trie

        # Build the Trie containing the words in the dictionary
        # Time Complexity: O(m * t)
        # Space Complexity: O(m * t)
        for word in wordDict:
            cur_node = self.root
            for c in word:
                next_trie_node = cur_node.children.get(c)

                if next_trie_node is None:
                    # Create the next Trie Node
                    next_trie_node = Trie()
                    cur_node.children[c] = next_trie_node
                
                # Move the cur_node to the next character Node
                cur_node = next_trie_node
            
            # Reached the end of the current word -> Mark it as a Leaf Trie Node
            cur_node.isEndOfWord = True
        
        '''
        Now, we have a Trie containing all the characters from the wordDict. All that is left is to iterate the target string 
        s and see if s can be split into words from wordDict
        '''
        return self.build_s(s, self.root)
    
    '''
    n <- length of s
    m <- Nº words in wordDict
    t <- Max length of word in wordDict

    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    '''
    def build_s(self, s: str, trie_root: Trie) -> bool:
        if not s:
            # If the Target string is empty -> We can build s from characters of the Trie -- Base case
            return True
        
        if s in self.memo:
            # If this solution was already attempted -> Return False
            return False

        cur_node = trie_root
        # Time Complexity: O(n * m)
        for idx in range(len(s)):
            c = s[idx]

            next_node = cur_node.children.get(c)
            if next_node is None:
                # Add solution to the memoized solutions
                self.memo.add(s)

                # Cannot build s with the Trie
                return False
            
            # Check if next_node is a a Leaf node of the Trie (end of a word from the dict)
            if next_node.isEndOfWord:
                # s may be built using this word
                if self.build_s(s[idx+1:], trie_root):
                    # If there is a solution using the remaining substring
                    return True
            
            # Update the cur_node
            cur_node = next_node
        
        # Add solution to memoized solutions
        self.memo.add(s)
        return False
        
            
            


res = Solution()

input1 = ["neetcode", ["neet", "code"]]
input2 = ["applepenapple", ["apple", "pen", "ape"]]
input3 = ["catsincars", ["cats", "cat", "sin", "in", "car"]]

sol = res.wordBreak(input1[0], input1[1])

print("Solution: ", sol)