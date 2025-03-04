from typing import *
import math
from collections import deque
from utils import Node, build_graph_from_adj_list, build_adj_list_from_graph

"""
Course Schedule
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a graph from this and check if there are no back edges?

        graph_nodes: list['Node'] = []

        # Create the numCourses nodes
        for node_idx in range(numCourses):
            graph_nodes.append(Node(node_idx, []))

        # Add the edges
        for cond in prerequisites:
            src, target = cond

            graph_nodes[src].neighbors.append(graph_nodes[target])

        # Check if there is a back edge (a node is visited more than once)
        def dfs(curr_node: 'Node', visited_nodes: Set['Node']):
            if curr_node in visited_nodes:
                # Not the first time
                return False

            visited_nodes.add(curr_node)

            for neigh in curr_node.neighbors:
                if not dfs(neigh, visited_nodes.copy()):
                    return False
            
            # Here, we know that the curr_node has no back edges, so let's remove all the edges to remove unnecessary work
            # Optimization step
            curr_node.neighbors = []

            return True

        for node in graph_nodes:
            if not dfs(node, set()):
                return False

        return True


res = Solution()

input1 = (2, [[0,1]])
input2 = [2, [[0,1],[1,0]]]
input3 = [5, [[1,4],[2,4],[3,1],[3,2]]]
input4 = [8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]]

sol = res.canFinish(input3[0], input3[1])

print("Solution: ", sol)

