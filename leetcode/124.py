from typing import *
import math
from utils import TreeNode, get_bfs_node, list_to_tree, print_bfs_tree, tree_to_list
from collections import deque

"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root or root.val == None:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Check if the solution where we split at the current node is the maximum solution
            res = max(res, root.val + leftMax + rightMax)

            # Return the max path sum going through this node and not splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res
        

res = Solution()

input1 = [1,2,3]
input2 = [-15,10,20,None,None,15,5,-5]
input3 = [-3]
input4 = [2,-1]
input5 = [-2,-1]
input6 = [-10,9,20,None,None,15,7]
input7 = [-2,None,-3]
input8 = [0]
input9 = [1,-2,-3,1,3,-2,None,-1]

tree_input1 = list_to_tree(input9)
print_bfs_tree(tree_input1)

sol = res.maxPathSum(tree_input1)

print("Solution: ", sol)