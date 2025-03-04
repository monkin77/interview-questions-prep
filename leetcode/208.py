from typing import *
import math
from collections import deque
import heapq

"""
Implement Prefix Tree
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""
class TreeNode:
    def __init__(self, is_end_of_word: bool = False):
        self.children: dict[str, TreeNode] = {}
        self.is_end_of_word: bool = is_end_of_word

"""
Trie
"""
class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                # If curr prefix is not saved in the Tree of chars
                curr_node.children[char] = TreeNode()
            
            # Set curr_node to the Node pointing to the last visited char
            curr_node = curr_node.children[char]
        
        curr_node.is_end_of_word = True # Declare the end of the current word

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
        
            curr_node = curr_node.children[char]
        
        return curr_node.is_end_of_word     # Word is found if we reached a leaf of the Tree of chars

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
        
            curr_node = curr_node.children[char]
        
        return True         # Word is found if we traverse the tree successfully up until prefix

prefixTree = PrefixTree()
prefixTree.insert("dog")
prefixTree.search("dog")    # return true
prefixTree.search("do")     #  return false
prefixTree.startsWith("do") #  return true
prefixTree.insert("do")
prefixTree.search("do")     #  return true

