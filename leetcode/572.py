from typing import *
import math
from utils import TreeNode, list_to_tree, print_dfs_tree, tree_to_list

"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1) -> If the subroot was completely found and remaining subtree from the root is empty
        if not (root or subRoot):
            return True
        # Base case 2) -> If the curr search node reached the end of the traversal and subRoot is not empty
        if not root:
            return False
        # Base case 3) -> Subroot was completely found but the root is not empty (subtree did not finish)
        if root and (not subRoot):
            return False
        
        # Variable that holds whether the solution starting in this node is viable
        curr_sol_start = False
        if root.val == subRoot.val:
            curr_sol_start = self.isSubtreeContinous(root.left, subRoot.left) and self.isSubtreeContinous(root.right, subRoot.right)

        if curr_sol_start:
            return True
        # Else: Search for the solution without using this node

        # If the curr node is not the same -> Search for the subtree in either the left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSubtreeContinous(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1) -> If the subroot was completely found and remaining subtree from the root is empty
        if not (root or subRoot):
            return True
        # Base case 2) -> If the curr search node reached the end of the traversal and subRoot is not empty
        if not root:
            return False
        # Base case 3) -> Subroot was completely found but the root is not empty (subtree did not finish)
        if root and (not subRoot):
            return False
        
        # Variable that holds whether the solution starting in this node is viable
        if root.val == subRoot.val:
            return self.isSubtreeContinous(root.left, subRoot.left) and self.isSubtreeContinous(root.right, subRoot.right)
        
        return False




res = Solution()

input1 = ([1,2,3,4,5], [2,4,5])
input2 = ([1,2,3,4,5,None,None,6], [2,4,5])
input3 = ([1,1], [1])
input4 = ([3,4,5,1,None,2], [3,1,2])

tree_input1 = list_to_tree(input4[0])
tree_input2 = list_to_tree(input4[1])

# print_dfs_tree(tree_input1)

sol = res.isSubtree(tree_input1, tree_input2)

print("Solution: ", sol)