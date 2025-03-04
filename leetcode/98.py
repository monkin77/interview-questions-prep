from typing import *
import math
from utils import TreeNode, get_bfs_node, list_to_tree, print_bfs_tree, tree_to_list
from collections import deque

"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubtree(root, None, None)
        
    def isValidSubtree(self, root: Optional[TreeNode], minVal, maxVal) -> bool:
        # Base case 1) if root is null, it is a valid BST
        if not root:
            return True
        
        if root.left and root.left.val and root.left.val >= root.val:
            # If the left node is >= root
            return False
        
        if root.right and root.right.val and root.right.val <= root.val:
            # If the right node is <= root
            return False
        
        is_curr_valid = (root.val == None) or ( ((minVal == None) or (minVal < root.val) ) and ( (maxVal == None) or (maxVal > root.val)) )

        return is_curr_valid and self.isValidSubtree(root.left, minVal, root.val) and self.isValidSubtree(root.right, root.val, maxVal)


res = Solution()

input1 = [2,1,3]
input2 = [1,2,3]
input3 = [5,4,6,None,None,3,7]

tree_input1 = list_to_tree(input1)
print_bfs_tree(tree_input1)

sol = res.isValidBST(tree_input1)

print("Solution: ", sol)