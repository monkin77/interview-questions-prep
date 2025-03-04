from typing import *
import math
from utils import TreeNode, get_bfs_node, list_to_tree, print_bfs_tree, tree_to_list
from collections import deque

"""
Level Order Traversal of Binary Tree
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        sol_list = []

        node_queue: Deque[TreeNode] = Deque()
        node_queue.append(root)

        while len(node_queue) > 0:
            # The number of nodes in the queue at the start of each level will dictate how many nodes we pick from it
            num_curr_level_nodes = len(node_queue)

            level_nodes = []    # Store the nodes of this level
            for _ in range(num_curr_level_nodes):
                # Using a Deque makes the pop operationg from the beggining O(1) instead of O(n)
                curr_node = node_queue.popleft()

                if curr_node.val != None:
                    # Add the children to the queue of nodes to be visited
                    if curr_node.left:
                        node_queue.append(curr_node.left)

                    if curr_node.right:
                        node_queue.append(curr_node.right)

                    level_nodes.append(curr_node.val)

            # See if the currLevel is only Filler TreeNodes
            if level_nodes:
                sol_list.append(level_nodes)    # Add the list with the nodes from this level
            
        return sol_list


res = Solution()

input1 = [1,2,3,4,5,6,7]
input2 = [1]
input3 = []
input4 = [1,2,None,3,None,4,None,5]

tree_input1 = list_to_tree(input4)
print_bfs_tree(tree_input1)

sol = res.levelOrder(tree_input1)

print("Solution: ", sol)