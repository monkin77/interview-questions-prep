#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

weight = 6

class Node:
    def __init__(self, ID, edges: set[int] = set()):
        self.ID = ID
        self.edges = edges
        self.dist = -1
        
    def add_edge(self, neighbor: int):
        self.edges.add(neighbor)

def bfs(n, m, edges, s):
    '''
    Parameters:
    --------
    n: num. nodes
    m: num. edges
    edges: list[tuples[src, dest]]
    s: start_node
    
    Returns: list[int] distances from s to all other nodes (ordered by node id number)
    '''
    # Write your code here
    
    # Create the nodes
    nodes = [Node(ident, set()) for ident in range(1, n+1)]
    visited = [False] * n
    startNode = nodes[s-1]
    startNode.dist = 0
    
    # Iterate edges and add to neighbors of nodes
    for edge in edges:
        start, dest = edge
        cur_node = nodes[start-1]
        dest_node = nodes[dest-1]
        
        # unordered graph, so edges are bi-directional
        cur_node.add_edge(dest)
        dest_node.add_edge(start)

        
    visit_queue: list[Node] = [startNode]
    while len(visit_queue) > 0:
        # print("Queue: ", visit_queue)
        cur_node = visit_queue.pop(0)
        if visited[cur_node.ID - 1]:
            # Skip it
            continue
            
        for dst_id in cur_node.edges:
            dst_node = nodes[dst_id-1]
            if visited[dst_id-1] or (dst_node in visit_queue):
                # Node already in queue or visited
                continue

            dst_node.dist = cur_node.dist + weight
            visit_queue.append(dst_node)
        
        visited[cur_node.ID-1] = True
        
    distances = []
    for node_idx in range(n):
        if node_idx+1 == s:
            # Skip the start node
            continue
        
        cur_node = nodes[node_idx]
        
        distances.append(cur_node.dist)
    
    return distances
    
    

if __name__ == '__main__':
    result = bfs(5, 5, [[1,2],[1,3], [2, 4], [3, 4], [1,5]], 1)

    print(' '.join(map(str, result)))
    print('\n')
