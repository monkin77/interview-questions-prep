import typing
from collections import deque

# ================= Binary Trees ============================= #
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(l: list[int]) -> TreeNode:
    if len(l) == 0:
        return None
    
    queue: list[TreeNode] = []  # Keep nodes that will be filled

    root = TreeNode(val=l[0])
    queue.append(root)
    l.pop(0)

    while len(l) > 0:
        filling_node = queue.pop(0)

        left_node = TreeNode(val = l[0])
        l.pop(0)

        right_node = None
        if len(l) > 0:
            right_node = TreeNode(val = l[0])
            l.pop(0)
        
        filling_node.left = left_node
        queue.append(left_node)
        if right_node:
            filling_node.right = right_node

            if right_node.val != None:
                # Only keep filling for this one if not a filler node
                queue.append(right_node)
    
    return root

def tree_to_list(root: TreeNode) -> list[TreeNode]:
    if not root:
        return []

    res = []
    queue: list[TreeNode] = []
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        res.append(curr_node.val)

        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return res

# Breadth-First Search 
def print_bfs_tree(root: TreeNode) -> None:
    if not root:
        return
    
    curr_node = root
    queue: list[TreeNode] = []
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        print(f"{curr_node.val}-", end="")

        has_child = curr_node.left or curr_node.right

        if curr_node.left:
            queue.append(curr_node.left)
        elif has_child:
            # If there is one child
            queue.append(TreeNode(val=None))

        if curr_node.right:
            queue.append(curr_node.right)
        elif has_child:
            # If there is one child
            queue.append(TreeNode(val=None))
    
    print()

def get_bfs_node(root: TreeNode, search_val: int) -> TreeNode:
    if not root: return None

    curr_node = root
    queue: list[TreeNode] = []
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        if curr_node.val == search_val:
            return curr_node

        has_child = curr_node.left or curr_node.right

        if curr_node.left:
            queue.append(curr_node.left)
        elif has_child:
            # If there is one child
            queue.append(TreeNode(val=None))

        if curr_node.right:
            queue.append(curr_node.right)
        elif has_child:
            # If there is one child
            queue.append(TreeNode(val=None))
    
    return None
    

    





# ================= Linked Lists ============================= #

# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

class DoublyListNode: 
    def __init__(self, val=0, next = None, prev = None):
         self.val = val
         self.next = next
         self.prev = prev


def list_to_linked_list(l) -> ListNode:
    if len(l) == 0:
        return None
    
    prevNode = None
    head = None
    for i in range(len(l)):
        currNode = ListNode(l[i], None)
        if head == None:
            head = currNode
            # Save the head of the list

        if prevNode:
            # Add the next node to the previous node
            prevNode.next = currNode
        
        prevNode = currNode

    return head

# ================= Graphs ============================= #

class Node:
    """
    Using a forward reference to point the type of neighbors as Nodes
    """
    def __init__(self, val: int, neighbors: list['Node']):
        self.val = val
        self.neighbors = neighbors

def build_graph_from_adj_list(adj_list: list[list[int]]) -> Node | None:
    if len(adj_list) == 0:
        return None
    
    # Create the list of nodes
    graph_nodes = [Node(val, []) for val in range(1, len(adj_list)+1, 1)]

    for node_idx in range(len(adj_list)):
        curr_node = graph_nodes[node_idx]

        # Update the neighbors using the adjency list
        curr_node.neighbors = [graph_nodes[neighbor_idx-1] for neighbor_idx in adj_list[node_idx]]

    # Return the input node
    return graph_nodes[0]

def build_adj_list_from_graph(node: Node) -> Node | None:
    if not node:
        return []
    
    adj_list = []

    node_list = deque([node])
    while len(node_list) > 0:
        curr_node: Node = node_list.popleft()

        adj_vals = [neighbor.val for neighbor in curr_node.neighbors]
        adj_list.append(adj_vals)

        for neighbor in curr_node.neighbors:
            if neighbor.val > curr_node.val:
                node_list.append(neighbor)
    
    return adj_list
