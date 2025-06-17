from typing import *

'''
Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0 or len(heights[0]) == 0:
            return []

        h, w = len(heights), len(heights[0])

        def dfs(i, j, visited_set, prev_height):
            '''
            Depth-First Search Traversal, adding the visited nodes to the set passed as a
            parameter.
            Only Visit neighbors with a height >= than the previous (water flow reversed)
            '''
            if ((i, j) in visited_set) or (
                i < 0 or i >= h or j < 0 or j >= w) or heights[i][j] < prev_height:
                return

            # Add current Cell to the visited set
            visited_set.add((i,j))

            # Visit neighbors
            dfs(i+1, j, visited_set, heights[i][j])
            dfs(i-1, j, visited_set, heights[i][j])
            dfs(i, j-1, visited_set, heights[i][j])
            dfs(i, j+1, visited_set, heights[i][j]) 

        # Create set of visited cells starting on a Cell bordering each Ocean
        pacific_set = set()
        atlantic_set = set()

        for col in range(w):
            dfs(0, col, pacific_set, heights[0][col])    # Visit all nodes starting from upper border
            dfs(h-1, col, atlantic_set, heights[-1][col]) # Visit all nodes starting from lower border
        for row in range(h):
            dfs(row, 0, pacific_set, heights[row][0])  # Visit all nodes starting from left border
            dfs(row, w-1, atlantic_set, heights[row][-1])   # Visit all nodes starting from right border

        # Check which cells are present on both sets
        results=[]
        for row in range(h):
            for col in range(w):
                if ((row, col) in pacific_set) and ((row, col) in atlantic_set):
                    results.append((row, col))
        
        return results

