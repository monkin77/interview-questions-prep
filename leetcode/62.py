from typing import *
import math

"""
Count Paths
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        We can build each row starting at the last one (where the target is)
        Each row will depend on the values of the previous row and the current row only
        """
        # Set the solutions of the last row to 1 (only 1 possible way)
        prev_row = [1] * n
        


        for _ in range(m - 1):
            newRow = [1] * n
            # Iterate the row for each column starting at the end
            # uniquePaths(i, j) = uniquePaths(i, j+1) + uniquePaths(i+1, j) -- Solutions on the right and down 
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + prev_row[j]
            prev_row = newRow

        return prev_row[0]

    def uniquePaths_intuitive(self, m: int, n: int) -> int:
        """
        Top-Down Approach: Starting at (m, n) we can either go down or right at every cell. Thus, we can derive the recurrence relation:
            - uniquePaths(m, n) = 2 + uniquePaths(m-1, n) + uniquePaths(m, n-1)
            - Edge cases: If m == 0: Can only move right. Elif n == 0: Can only move down.
            - Base case: when m == n == 0: return 0 (no more paths)

            We are subtracting m and n when we go recursively to avoid avoid 2 extra variables to the current row and column. Thinking about it backwards will lead to the same
        """
        # Store partial solutions
        dp: list[list[int]] = [[None] * n] * m

        partial_sol = dp[m-1][n-1]
        if partial_sol != None:
            # Arrived at partial solution that was already calculated
            return partial_sol

        # Base case 1)
        if m == n == 1:
            # Arrived at the end point
            dp[m-1][n-1] = 1
            return 1
        
        if m == 1:
            # Can only move right
            num_paths = self.uniquePaths(m, n-1)

            dp[m-1][n-1] = num_paths
            return num_paths
        
        if n == 1:
            # Can only move down
            num_paths = self.uniquePaths(m-1, n)

            dp[m-1][n-1] = num_paths
            return num_paths
        
        # Check the solutions going down and right
        num_paths = self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

        dp[m-1][n-1] = num_paths
        return num_paths
        
       


res = Solution()

input1 = (3, 6)
input2 = (3, 3)

sol = res.uniquePaths(input1[0], input1[1])

print("Solution: ", sol)