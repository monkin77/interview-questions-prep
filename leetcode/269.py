from typing import *
import math
from collections import deque
from utils import Node, build_graph_from_adj_list, build_adj_list_from_graph

"""
Foreign Dictionary
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
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
    
    """
    Returns the char where the newWord differs from the existing words in the Trie
    Return:
        Tuple (index where newWord differs, list of strings with the same prefix up until that point)
        if idx == -1: newWord is empty
        if idx >= len(newWord): The new word is a prefix of an existing word (could also be equal)
    """
    def findDifferingChar(self, newWord) -> Tuple[int, list[str]]:
        if len(newWord) == 0: return -1

        curr_node = self.root
        for idx, char in enumerate(newWord):
            if char not in curr_node.children:
                return (idx, curr_node.children.keys()) 
            
            curr_node = curr_node.children[char]
        
        return (idx+1, curr_node.children)
    
    def findDifferingIdx(self, newWord, prevWord) -> int:
        if len(newWord) == 0: return -1

        for idx, char in enumerate(newWord):
            if idx >= len(prevWord):
                return idx
            if char != prevWord[idx]:
                return idx
        
        return len(newWord)

class Solution:
    def __init__(self):
        self.trie = PrefixTree()
        self.nodes: Dict[str, Node] = {}    # Store the nodes of the graph that will represent the lexicographic order in a dict

    def foreignDictionary(self, words: List[str]) -> str:
        # We have to do 2 things: 
        # 1. Store the visited words in a Trie to retrieve the largest prefix fast
        # 2. Create a Graph that connects (s, t), where s is a character < t and update it

        existing_chars: Set[str] = set()

        for word_idx, word in enumerate(words):
            for char in word:
                # Add all the existing characters to the set
                existing_chars.add(char)

                # Check if the current character already has an outgoing edge to another node (meaning that )

            diff_idx, diff_chars = self.trie.findDifferingChar(word)
            if diff_idx == -1: continue     # The new word is empty so we skip it

            diff_idx_prev = self.trie.findDifferingIdx(word, words[word_idx-1])
            if word_idx > 0 and diff_idx != diff_idx_prev:
                print("Order is not valid")
                return ""

            if diff_idx < len(word):
                c = word[diff_idx]  # The character where the diff appears

                # Add the new character to the Graph of Nodes if it does not exist
                diff_node = None
                if c in self.nodes:
                    diff_node = self.nodes[c]
                else:
                    diff_node = Node(c, [])
                    self.nodes[c] = diff_node

                # The new word shares a prefix with an existing one ( COULD BE AN: "" )
                for char in diff_chars:
                    # If there isn't still a node with this char -> Create it
                    if char not in self.nodes:
                        self.nodes[char] = Node(char, [])

                    # We iterate the differing chars to create the connections on the graph
                    self.nodes[char].neighbors.append(diff_node)    # TODO: Could it be optimized to create less edges?
            elif diff_idx == len(word):
                if diff_chars == {}:
                    # Duplicated word (already added this one)
                    continue

                # The new word is a prefix of an existing word
                # This cannot happen because the words are sorted according to them. So a prefix of an existing word cannot occur -> INVALID
                return ""

            # Add new word to the Prefix Tree (Trie)
            self.trie.insert(word)

        # Derive the order of the letters in the dictionary based on the Graph (node without input edges (INDEGREE 0) comes first)
        # If there is a loop: INVALID
        node_keys = self.nodes.keys()
        indegrees: dict[str, int] = {c: 0 for c in node_keys}
        for curr_node in self.nodes.values():
            for neigh in curr_node.neighbors:
                indegrees[neigh.val] += 1   # Increment the neighbor indegree by 1
        
        # print("Indegrees: ", indegrees)
        queue: Deque[Node] = deque([])   # Queue holding the nodes with INDEGREE = 0. We are going to see if there are no loops in the graph and create the order for the characters
        order = ""
        for node in [self.nodes[char] for (char, deg) in indegrees.items() if deg == 0]:
            queue.append(node)
        
        while len(queue) > 0:
            pop_node = queue.popleft()

            order += pop_node.val   # Add the char to the lexicographic order

            for neigh in pop_node.neighbors:
                indegrees[neigh.val] -= 1
                if indegrees[neigh.val] == 0:
                    queue.append(neigh)
        
        if len(order) != len(self.nodes):
            # Some nodes were not popped (INDEGREE > 0)
            return ""   # INVALID
        
        if len(existing_chars) > len(order):
            # There are characters that we did not find the order, so we can assume any
            # Let's append at the end of the word
            for existing_char in existing_chars:
                if existing_char not in self.nodes:
                    order += existing_char

        # If valid
        return order
            



res = Solution()

input1 = ["z","o"]
input2 = ["hrn","hrf","er","enn","rfnn"]
input3 = ["abc","bcd","cde"]
input4 = ["z","z"]
input5 = ["abcdefgh","bdefghij","cghij","dfghij","efghij","fghij","ghij","hij","ij","j","abcdefghi","bdefghijk","cghijk","dfghijk","efghijk","fghijk","ghijk","hijk","ijk","jk","k"]

sol = res.foreignDictionary(input2)

print("Solution: ", sol)

