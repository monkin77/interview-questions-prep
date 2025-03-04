from typing import *
import math
from utils import TreeNode, list_to_tree, tree_to_list

"""
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


res = Solution()

input1 = [1,2,3,None,None,4]
input2 = []
input3 = []

tree_input = list_to_tree(input1)

sol = res.maxDepth(tree_input)

print("Solution: ", sol)