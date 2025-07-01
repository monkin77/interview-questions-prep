from typing import *
from utils import TreeNode, list_to_tree
import ast
from math import log2, ceil

"""
Serialize and Deserialize Binary Tree
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.
"""
class Codec:
    def count_all_nodes(self, root: Optional[TreeNode]) -> int:
        if root is None or root.val is None:
            return 0
        
        return 1 + self.count_all_nodes(root.left) + self.count_all_nodes(root.right)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree_list: list[int] = []

        if not root:
            return str(tree_list)
        
        total_nodes = self.count_all_nodes(root)

        node_count = 0

        visit_q: list[Optional[TreeNode]] = [root]
        while len(visit_q) > 0 and node_count < total_nodes:
            # pop first node in the queue
            cur_node: Optional[TreeNode] = visit_q.pop(0)

            # Check if cur_node is None
            if cur_node is None or cur_node.val is None:
                # Add None to the tree_list and go to the next elem
                tree_list.append(None)
                continue
            #else:
            #    num_nodes += 1
            #    cur_depth_nodes -= 1

            # Add node val to the tree_list
            tree_list.append(cur_node.val)
            node_count += 1

            # Add Left and Right nodes to the visit queue
            visit_q.append(cur_node.left)
            visit_q.append(cur_node.right)
        
        
        
        return str(tree_list)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convert serialized list into a list
        tree_list = ast.literal_eval(data)

        if len(tree_list) == 0:
            return None
        
        root_node = TreeNode(tree_list[0])
        cur_node = None # Keeps tracks of cur_node
        visit_q: list[Optional[TreeNode]] = [root_node]

        # Level-order Traversal. Each node has 2 children, so we iterate 2 by 2
        # We need to add 1 to the edge of the range for the edge case of having 1 element?
        for i in range(1, len(tree_list), 2):
            # Iterate the whole tree_list starting from the second element
            cur_parent = visit_q.pop(0)

            # left child
            left_node = TreeNode(tree_list[i])
            # check if there is a right child
            right_node = None
            if i+1 < len(tree_list):
                right_node = TreeNode(tree_list[i+1])

            cur_parent.left = left_node
            cur_parent.right = right_node

            # Add new nodes to the visit_q
            visit_q.append(left_node)
            visit_q.append(right_node)
        
        return root_node
        

res = Codec()

input1 = res.deserialize("[1,2,3,None,None,4,5]")
input2 = res.deserialize("[]")
input3 = res.deserialize("[1,2,3, None, None, 4, 5, 6, None]")

sol_encode = res.serialize(input3)
print("Sol encode: ", sol_encode)

sol_decode = res.serialize(res.deserialize(sol_encode))
print("sol_decode: ", sol_decode)

# NOTE: This is not working because the list_to_tree method converts a list to a 