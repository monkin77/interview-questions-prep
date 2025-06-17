from typing import *
from utils import TreeNode, tree_to_list

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Overall Time Complexity: O(n^2) due to recursive calls in last case scenario
        Space Complexity: O(n) - Context of each recursive call
        '''
        # Base case
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # Define pivot (root)
        root_val = preorder[0]

        # Find index of the root node in the in-order list - Time Complexity: O(n)
        inorder_root_idx = len(inorder)-1  # Default value in case we don't find the pivot
        for idx, node_val in enumerate(inorder):
            if node_val == root_val:
                inorder_root_idx = idx
                # stop searching
                break
        # Calculate nº of nodes in the left subtree
        num_left_nodes = inorder_root_idx
            
        '''We now know that the left subtree has num_left_nodes nodes. So we can already split both lists into
        the subtrees'''
        preorder_pivot_idx = num_left_nodes + 1 # Add 1 to include the root node

        # Split the inorder traversal list into left-and-right lists according to the root node index
        left_nodes_inorder = inorder[:inorder_root_idx]
        right_nodes_inorder = inorder[inorder_root_idx+1:]
                
        # Split the Preorder traversal list into left-and-right according to 
        # the Rightmost Node before Root index
        left_nodes_preorder = preorder[1:preorder_pivot_idx] # Skip the root node
        right_nodes_preorder = preorder[preorder_pivot_idx:]

        # Recursively compute the left and right subtree and define the Root Node - Time Complexity: O(n)
        left_tree = self.buildTree(left_nodes_preorder, left_nodes_inorder)
        right_tree = self.buildTree(right_nodes_preorder, right_nodes_inorder)
        root_node = TreeNode(root_val, left_tree, right_tree)
        return root_node

res = Solution()
input1 = [[1,2,3,4], [2,1,3,4]]
input2 = [[1], [1]]
input3 = [[1,2,3,4,5],[5,4,3,2,1]]

sol = res.buildTree(input3[0], input3[1])

print("Solution: ", tree_to_list(sol))