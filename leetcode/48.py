from typing import *

'''
Rotate Image
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) # num. rows = num. cols

        # We can floor the value since if odd -> last dimension (1x1) 
        # matrix remains the same
        num_outer_modifications = n // 2
        # Time Complexity: O(log n)
        for outer_mod_idx in range(num_outer_modifications):
            matrix_size = n - outer_mod_idx * 2
            
            # Ti
            # Get the Rows
            top_row = matrix[outer_mod_idx][outer_mod_idx:outer_mod_idx + matrix_size]
            bottom_row = matrix[n-outer_mod_idx-1][outer_mod_idx:outer_mod_idx + matrix_size]
            
            # Get the Cols
            left_col = [matrix[i+outer_mod_idx][outer_mod_idx] for i in range(matrix_size)]
            right_col = [matrix[i+outer_mod_idx][n-1-outer_mod_idx] for i in range(matrix_size)]

            # Perform the 90º rotation
            # Top Row -> Right Col and Bottom Row -> Left col
            for i in range(matrix_size):
                matrix[i+outer_mod_idx][n-1-outer_mod_idx] = top_row[i]   # New Right Col.

                matrix[i+outer_mod_idx][outer_mod_idx] = bottom_row[i]    # New Left Col.

            # Right Col -> Bottom Row - need to reverse the elements in right col
            matrix[n-outer_mod_idx-1][outer_mod_idx:outer_mod_idx + matrix_size] = right_col[::-1]
            # Left Col. -> Top Row
            matrix[outer_mod_idx][outer_mod_idx:outer_mod_idx + matrix_size] = left_col[::-1]

res = Solution()
input1 = [
  [1,2],
  [3,4]
]
input2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
input3 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

input = input3
res.rotate(input)

print("Solution: ", input)