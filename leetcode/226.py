from typing import *
import math
from utils import TreeNode, list_to_tree, tree_to_list

"""
You are given the root of a binary tree root. Invert the binary tree and return its root.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case (1)
        if not root:
            return None
        
        # Recursive step
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        # Invert the left and right nodes (Joining Step)
        tmp_left = root.left
        root.left = root.right
        root.right = tmp_left

        # Base case (2)
        return root


res = Solution()

input1 = [1,2,3,4,5,6,7]
input2 = [3,2,1]
input3 = []

tree_input = list_to_tree(input1)

sol = res.invertTree(tree_input)

sol_list = tree_to_list(sol)

print("Solution: ", sol_list)