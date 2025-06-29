from typing import *
import numpy as np

'''
Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
'''
class Solution:
    '''
    Time Complexity: O(E + N)
    Space Complexity: O(N)
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        # Time Complexity: O(E)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, prev):
            '''
            Recursively Traverse the graph using DFS and check if there are any cycles.
            '''
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        # Time Complexity: O(N)
        return dfs(0, -1) and len(visit) == n  

    '''
    Time Complexity: O(E + N)
    Space Complexity: O(N^2)
    '''
    def validTree_parents(self, n: int, edges: List[List[int]]) -> bool:
        # Stores a list of parents for each node
        parents: list[set[int]] = [set() for i in range(n)]

        # Time Complexity: O(E)
        for edge in edges:
            # Order edges by Node Value so that we can use only upper triangle of the matrix
            start = min(edge[0], edge[1])
            end = max(edge[0], edge[1])
            # This means start will be the parent of end

            # Time Complexity O(1)
            if start in parents[end]:
                # If start was already a parent of end -- found a new path to end -- invalid tree
                return False
            # Time Complexity: O(N)
            # if len(parents[start].intersection(parents[end])) > 0:
            #     # Check if new node already has a common parent -> If so -- invalid tree
            #     return False
            prev_parents_start_len = len(parents[start])
            prev_parents_end_len = len(parents[end])

            # Update the parents list
            parents[end].update(parents[start]) # Add Previous Ancestors
            parents[start] = parents[start].union(parents[end])
            parents[end].add(start) # Add direct ancestors

            if len(parents[end]) < prev_parents_end_len + 1 + prev_parents_start_len:
                # The intersections between the parent sets was not empty -> invalid
                return False

        for node in range(1, n):
            if 0 not in parents[node]:
                return False
        return True
            


    def prevValidTree(self, n: int, edges: List[List[int]]) -> bool:
        dp: np.array = np.full((n, n), fill_value=-1)   # initialize distances as -1

        # Edges are bidirectional, so we will only use the upper triangle of distances
        for edge in edges:
            # Define start and end based on Node Value to use only upper triangle
            start = min(edge[0], edge[1])
            end = max(edge[0], edge[1])

            if dp[start][end] != -1:
                # Distance was already defined -> found an extra path
                # Invalid tree
                return False
            
            # Otherwise, update the distance between the Node pair
            dp[start][end] = 1

            '''
            Update the distance between nodes.
            Find prev edges with endNode = start
            '''
            for prev_start_id in range(start-1, -1, -1):
                for prev_end_id in range(end-1, -1, -1):
                    if dp[prev_start_id, prev_end_id] != -1:
                        # Can add distance
                        dp[prev_start_id, end] = 1 + dp[prev_start_id, prev_end_id]
                        break
            
        # Check if all distances are > 0
        # return np.all(dp > 0)
        return True
                

res = Solution()
input1 = (5, [[0, 1], [0, 2], [0, 3], [1, 4]])
input2 = (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
input3 = (5, [[0,1],[0,2],[1,2],[3,4]])
input4 = (4, [[0,1],[2,3]])
input5 = (5, [[0,1],[1,3],[3,2],[1,4]])

sol = res.validTree(input5[0], input5[1])

print("Solution: ", sol)