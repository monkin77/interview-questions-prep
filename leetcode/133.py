from typing import *
import math
from collections import deque
from utils import Node, build_graph_from_adj_list, build_adj_list_from_graph

"""
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.cloneGraphAux(node, {})
    
    """
    params:
    - visitedNodes: Map of node value to the node
    """
    def cloneGraphAux(self, node: Optional['Node'], visitedNodes: Dict[int, Node]) -> Optional['Node']:
        if not node:
            return None

        # create the new node
        newNode = Node(node.val, [])

        # Add it to the visited map
        visitedNodes[newNode.val] = newNode

        # Build the neighbors
        newNeighbors = []
        for neighbor in node.neighbors:
            if neighbor.val in visitedNodes:
                newNeighbors.append(visitedNodes[neighbor.val])
            else:
                newNeighbors.append(self.cloneGraphAux(neighbor, visitedNodes))

        newNode.neighbors = newNeighbors

        return newNode

res = Solution()

input1 = [[2],[1,3],[2]]
input2 = [[]]
input3 = []


input_node = build_graph_from_adj_list(input1)

sol = res.cloneGraph(input_node)

sol_adj_list = build_adj_list_from_graph(sol)

print("Solution: ", sol_adj_list)

