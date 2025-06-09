from typing import *
import math

class TrieNode:
    def __init__(self):
        self.children: map[str, TrieNode] = {}    
        self.isLeaf = False     # Whether it's end of a word        

class WordDictionary:
    def __init__(self):
        # Create root node
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        '''
        Insert word in the Trie

        Time Complexity: O(n) where n is the length of the word
        Space Complexity: O(n) for storing the Trie Nodes
        '''
        curNode = self.root
        
        # Iterate the characters of the new string to insert (word)
        for c in word:
            if c not in curNode.children:
                # Create TrieNode and Add to the Trie Data Structure
                curNode.children[c] = TrieNode()

            # Update the current node to the next Character
            curNode = curNode.children[c]
        
        # After iterating through all the character Trie Nodes, set the last element as a leaf
        curNode.isLeaf = True

    def search(self, word: str) -> bool:
        '''
        Search for a word in the Trie.
        Supports replacing individual characters by a "."

        Time Complexity: O(n)*O(m) where n is the length of the word and m is the number of nodes in the Trie
        Space Complexity: O(n)*O(m) for storing the Trie Nodes
        '''
        # Define list of search pairs (root node, search key) where the
        # Trie might be storing the word
        searchPairs = [(self.root, word)]
        
        while len(searchPairs) > 0:
            foundKey = True # By default, the current searchPair is successful
            curNode, curKey = searchPairs.pop(0)

            for idx, c in enumerate(curKey):
                if c == '.':
                    # Add childNodes of curNode to possible searchPairs (any char works)
                    for childNode in curNode.children.values():
                        searchPairs.append((childNode, curKey[idx+1:]))

                    # Set foundKey to false since this pair is not the final verification
                    foundKey = False
                    break

                if c not in curNode.children:
                    # word not found in the Trie -> Go to next searchPair
                    foundKey = False
                    break
                    
                # Update the current node to the next character
                curNode = curNode.children[c]
            
            if foundKey and curNode.isLeaf:
                # If matched the whole key -> return True if it's a leaf node
                return True
            
        # No possible key match found
        return False

wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say")) # return false
print(wordDictionary.search("day")) # return true
print(wordDictionary.search(".ay")) # return true
print(wordDictionary.search("b..")) # return true