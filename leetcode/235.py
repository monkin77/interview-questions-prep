from typing import *
import math
from utils import TreeNode, get_bfs_node, list_to_tree, tree_to_list

"""
Lowest Common Ancestor in Binary Search Tree
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # To find the lowest common ancestor, we need to find the subtree where p and q part ways (split)
        
        # Base case 1) If root is none -> there is no common ancestor
        if not root:
            return None 
        
        curr_root = root
        last_ancestor = root    # Store the last common ancestor
        while curr_root:
            if p.val < curr_root.val and q.val < curr_root.val:
                # Search for the LCA (Lowest-Common Ancestor) on the left subtree
                curr_root = curr_root.left
            elif p.val > curr_root.val and q.val > curr_root.val:
                # Search for the LCA (Lowest-Common Ancestor) on the right subtree
                curr_root = curr_root.right
            else:
                # The split occurs here
                last_ancestor = curr_root
                break
        
        return last_ancestor



res = Solution()

input1 = ([5,3,8,1,4,7,9,None,2], 3, 8)
input2 = ([5,3,8,1,4,7,9,None,2], 3, 4)
input3 = ([1,1], [1])
input4 = ([3,4,5,1,None,2], [3,1,2])

tree_input1 = list_to_tree(input1[0])
node_input1 = get_bfs_node(tree_input1, input1[1])
node_input2 = get_bfs_node(tree_input1, input1[2])

# print_dfs_tree(tree_input1)

sol = res.lowestCommonAncestor(tree_input1, node_input1, node_input2)

print("Solution: ", sol.val)