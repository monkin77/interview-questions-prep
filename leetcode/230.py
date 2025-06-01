from typing import *
import math
from utils import TreeNode, list_to_tree, tree_to_list

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res


res = Solution()

input1 = ([2,1,3], 1)
input2 = ([4,3,5,2], 4)
input3 = []

tree_input = list_to_tree(input2[0])

sol = res.kthSmallest(tree_input, input2[1])

print("Solution: ", sol)