from typing import *
from copy import deepcopy

class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {} # dict of {char: Trie}
        self.isEndOfWord = False
    
    def add_word(self, word: str):
        cur_node = self
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Trie()
            
            # Update cur_node
            cur_node = cur_node.children[c]
        
        # Set last node as endOfWord
        cur_node.isEndOfWord = True

"""
Word Search II
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
"""
class Solution:
    '''
    Time Complexity: O(m * n * (4^t) + s)
    Space Complexity: O(s)

    m, n <- num_rows, num_cols
    t <- max length of a word
    s <- sum of the length of all words
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0 or len(board[0]) == 0:
            return []

        # Get the nº rows and cols
        ROWS, COLS = len(board), len(board[0])

        # Build Trie with the words we want to find
        trie_root = Trie()
        # Time Complexity: O(num_words * t) = O(s)
        # Space Complexity: O(s)
        for word in words:
            # Time Complexity: O(t)
            trie_root.add_word(word)    # Add each word to the Trie

        found_words: set[str] = set()

        def dfs(i, j, path: set[(int, int)], cur_trie_node: Trie, cur_word: str):
            '''
            Travels through the matrix without duplicates and searches for the words
            in the Trie.
            (i, j) corresponds to the next coordinates we attempt to visit

            Space Complexity: O(t) - The recursion depth never exceeds the length of the longest word
            '''
            # Check if the current matrix position includes relevant paths
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or ((i, j) in path):
                # Found dead end -> Out of bounds or already visited
                return
            next_c = board[i][j]
            if next_c not in cur_trie_node.children:
                # If the next character is not in the Trie -> No relevant words in this path
                return
            
            # Otherwise -> Valid path, let's keep going
            # Visit UP, RIGHT, DOWN, LEFT
            path.add((i, j))    # Add this node to the path
            # Update the Trie Node
            new_trie_node = cur_trie_node.children[next_c]
            # Update cur_word
            new_word = cur_word + next_c

            # Check if found a new word from the list
            if new_trie_node.isEndOfWord:
                found_words.add(new_word)

                # Remove endOfWord property from the Node since we don't have to look for it anymore
                new_trie_node.isEndOfWord = False

                if len(found_words) == len(words):
                    # Found all words
                    return

            # UP
            dfs(i-1, j, path, new_trie_node, new_word)
            # RIGHT
            dfs(i, j+1, path, new_trie_node, new_word)
            # DOWN
            dfs(i+1, j, path, new_trie_node, new_word)
            # LEFT
            dfs(i, j-1, path, new_trie_node, new_word)
            # Remove the visited node
            path.remove((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                if len(found_words) == len(words):
                    # Found all words
                    break
                dfs(i, j, set(), trie_root, "")

        return list(found_words)
    
res = Solution()

input1 = ([["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]], ["bat","cat","back","backend","stack"])

input2 = ([["x","o"],["x","o"]], ["xoxo"])



sol = res.findWords(input1[0], input1[1])

print("Solution: ", sol)