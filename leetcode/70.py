from typing import *
import math
from utils import TreeNode, get_bfs_node, list_to_tree, print_bfs_tree, tree_to_list
from collections import deque

"""
Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        # keep track of the number of ways for the last 2 steps
        prev2_steps, prev_step = 1, 1

        for i in range(n-1):
            temp = prev2_steps + prev_step  # New steps = sum the last 2 solutions (Fibonacci Sequence)
            prev2_steps = prev_step
            prev_step = temp

        return prev_step


res = Solution()

input1 = 2
input2 = 3
input3 = [5,4,6,None,None,3,7]

sol = res.climbStairs(input2)

print("Solution: ", sol)