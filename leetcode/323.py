from typing import *
import math

"""
Number of Connected Components in an Undirected Graph
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.edges: list['Node'] = []

    def add_neighbor(self, neigh: 'Node'):
        # Add neigh to the list of edges in both Nodes (Undirected edges)
        # NOTE: Not checking if it is already a neighbour, i.e., allows for
        # duplicate connections
        self.edges.append(neigh)
        neigh.edges.append(self)

class DSU:
    '''
    Union Find Solution
    '''
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents_unionFind(self, n: int, edges: List[List[int]]) -> int:
            dsu = DSU(n)
            res = n
            for u, v in edges:
                if dsu.union(u, v):
                    res -= 1
            return res


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ''' Build Graph from n and edges
        Time Complexity: O(n + E)
        Space Complexity: O(n + E)
        '''
        # Create list of Nodes from 0 to n-1
        # Time Complexity: O(n)
        nodes_list: list[Node] = [Node(i) for i in range(n)]

        # Update the neighbours in the Graph
        # Time Complexity: O(E)
        for edge in edges:
            start, end = edge
            start_node, end_node = nodes_list[start], nodes_list[end]
            # Adds connections between nodes
            start_node.add_neighbor(end_node)

        # initalize nº connected components
        num_components = 0
        # Create set containing the nodes that remain to be visited
        # Space Complexity: O(n)
        remaining_nodes: set[int] = set(list(range(n)))

        def dfs(cur_node: Optional[Node]):
            '''
            Dfs across the graph without visiting duplicate nodes
            Time Complexity: O(E)
            '''
            if not cur_node or (cur_node.value not in remaining_nodes):
                # If cur_node is None or it was already visited -> Stop recursion
                return

            # Visited this node -> remove it from remaining_nodes
            remaining_nodes.remove(cur_node.value)

            for neighbor in cur_node.edges:
                dfs(neighbor)

        # While there are nodes yet to be visited
        # Time Complexity: O(n + E)
        while len(remaining_nodes) > 0:       
            # Increment the nº of connnected components
            num_components += 1

            # Get next root
            next_root = nodes_list[next(iter(remaining_nodes))]

            # Dfs current tree
            dfs(next_root)

        return num_components
    

res = Solution()

input1 = (3, [[0,1],[0,2]])
input2 = (6, [[0,1],[1,2],[2,3],[4,5]])
input3 = ([1], 0)

sol = res.countComponents(input1[0], input1[1])

print("Solution: ", sol)