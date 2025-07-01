from typing import *
from unittest import TestResult
from copy import deepcopy

"""
Word Search
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
"""
class Solution:
    '''
    Time Complexity: O(m * (4^n))
    Space Complexity: O(n) - Max. Recursion depth of dfs
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Time Complexity: O(4^n), n = len(word)
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        # Time Complexity: O(m), m = length board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    def exist_inefficient(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return len(word) == 0
        if len(word) == 0:
            return True

        rows, cols = len(board), len(board[0])

        # Flatten index = row*num_cols + col
        visited_set: set[int] = set()   # Contains the visited nodes by their flattened index

        # Define the Recursive Function
        def find_word(visited: set[int], prev_c_idx: int, 
          remaining_word: str) -> bool:
            if len(remaining_word) == 0:
                return True
            
            # Check if sol is is invalid sols -> return False if so
            # if (prev_c_idx, remaining_word) in invalid_sols:
            #     return False

            def build_new_sol(row, col, visited: set[int], next_c):
                new_idx = row*cols+col
                if board[row][col] == next_c and new_idx not in visited:
                    visited.add(new_idx)
                    if find_word(visited, new_idx, remaining_word[1:]):
                        return True
                    else:
                        visited.remove(new_idx)
                return False
                    
            # calculate the matrix coords from int
            prev_row, prev_col = prev_c_idx // cols, prev_c_idx % cols

            # Check if modification is by reference or not
            next_c = remaining_word[0]

            # Visit every possible solution (move horizontal or vertically)
            # Move Right
            if prev_col < cols-1 and build_new_sol(prev_row, prev_col+1,
                visited, next_c):
                return True
            # Move Down
            if prev_row < rows-1 and build_new_sol(prev_row+1, prev_col,
                visited, next_c):
                return True
            # Move Left
            if prev_col > 0 and build_new_sol(prev_row, prev_col-1,
                visited, next_c):
                return True
            # Move Up
            if prev_row > 0 and build_new_sol(prev_row-1, prev_col,
                visited, next_c):
                return True
            
            # No solution found
            # Save solution
            # invalid_sols.add(repr(visited)) # TODO: CHeck
            return False


        # Call find_word for every occurence of the first character of the word
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    cur_idx = row*cols+col
                    visited_set.add(cur_idx)
                    if find_word(visited_set, cur_idx, word[1:]):
                        return True
                    else:
                        visited_set.remove(cur_idx)
        
        # If not found any solution -> return False
        return False

res = Solution()

input1 = ([
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
], "CAT")

input2 = ([
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
], "BAT")

input3 = ([["C","A","A"],["A","A","A"],["B","C","D"]]
          , "AAB")

input4 = ([["A","B","E"],["B","C","D"]], "ABCDEB")

sol = res.exist(input4[0], input4[1])

print("Solution: ", sol)