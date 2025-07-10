from typing import *
from utils import TreeNode, list_to_tree, print_bfs_tree
from collections import deque

"""
Same Binary Tree 
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Queue of shape [First Tree Queue, Second Tree Queue]
        traversal_queue: list[list[TreeNode]] = [[p], [q]]

        while len(traversal_queue[0]) + len(traversal_queue[1]) > 0:
            if len(traversal_queue[0]) == 0 or len(traversal_queue[1]) == 0:
                # One of the Trees became empty -> Trees do not have the same structure
                return False

            # While there are elements in a tree to visit
            next_p = traversal_queue[0].pop(0)
            next_q = traversal_queue[1].pop(0)

            if next_p is None and next_q is None:
                # Node is the same -> Empty node -> Leaf
                continue
            elif (next_p is None and next_q is not None) or (
                next_q is None and next_p is not None):
                # One of the nodes is None -> Invalid
                return False

            if next_p.val != next_q.val:
                # If node value does not match -> Not the same tree
                return False

            # Add left and right nodes to the traversal queue
            traversal_queue[0] += [next_p.left, next_p.right]
            traversal_queue[1] += [next_q.left, next_q.right]

        # If reached here -> valid tree
        return True


res = Solution()

input1 = ([1,2,3], [1,2,3])
input2 = ([4,7], [4, None, 7])
input3 = ([1,2,3], [1,3,2])

tree_input1 = (list_to_tree(input1[0]), list_to_tree(input1[1]))
print_bfs_tree(tree_input1[0])

sol = res.isSameTree(tree_input1[0], tree_input1[1])

print("Solution: ", sol)