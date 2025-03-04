from typing import *
import math

"""
Set Zeroes in Matrix
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0:
            return

        coords = []

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        # Find the coords of all the 0's in the matrix
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    coords.append((i, j))


        # For each zero, update the original matrix accordingly
        for r, c in coords:
            # Update the row
            matrix[r][:] = [0 for _ in range(num_cols)]

            # Update the Column
            for row in range(num_rows):
                matrix[row][c] = 0
        
        return
    
    def setZeroesEfficient(self, matrix: List[List[int]]) -> None:
        """
        O(1) Space Complexity
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


res = Solution()

input1 = [
  [0,1],
  [1,1]
]
input2 = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

res.setZeroes(input2)

print("Solution: ", input2)