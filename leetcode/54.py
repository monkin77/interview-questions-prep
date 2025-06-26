from typing import *

'''
Spiral Matrix
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.
'''
class Solution:
    '''
    Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix.
    Space Complexity: O(m*n) for the output list.
    This is because we are storing all elements of the matrix in the output list.
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        # Pointers for the bounding box
        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1

        visited: list[int] = [] # List of visited elements

        while True:
            # Left-to-right
            if left > right:
                # If left edge is > right edge -> cannot go left anymore
                break   # Should I break or check the other conditions?
            
            visited_left_to_right = matrix[top][left:right+1]
            # add visited nodes to the list
            visited += visited_left_to_right
            # Update the Top pointer
            top += 1

            # Top-to-Bottom
            if top > bottom:
                # cannot add more
                break
            # collect visited elements
            visited_top_to_bottom = []
            for idx in range(top, bottom+1):
                visited_top_to_bottom.append(matrix[idx][right])
            # Add visited nodes to the list
            visited += visited_top_to_bottom
            # Update the Right pointer
            right -= 1

            # Right-to-Left
            if left > right:
                # If left edge is > right edge -> cannot go right anymore
                break
            # Reverse the visiting order
            visited_right_to_left = matrix[bottom][left:right+1][::-1]
            # Add visited nodes to the list
            visited += visited_right_to_left
            # Update the Bottom pointer
            bottom -= 1

            # Bottom-to-Top
            if top > bottom:
                # Cannot add more
                break
            # collect visited elements
            visited_bottom_to_top = []
            for idx in range(bottom, top-1, -1):
                # Iterate from bottom to top element
                visited_bottom_to_top.append(matrix[idx][left])
            # Add visited nodes to the list
            visited += visited_bottom_to_top
            # Update the Left pointer
            left += 1

        return visited


            

res = Solution()
input1 = [[1,2],[3,4]]
input2 = [[1,2,3],[4,5,6],[7,8,9]]
input3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

sol = res.spiralOrder(input2)

print("Solution: ", sol)