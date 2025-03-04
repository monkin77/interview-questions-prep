class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrderRec(root):
    #Write your code here
    if root == None:
        return ""
        
    preOrderStr = str(root.info)
    
    # Recursively go to left tree
    if root.left:
        preOrderStr += f" {preOrderRec(root.left)}" 
    
    if root.right:
        # Recursively go to right tree
        preOrderStr += f" {preOrderRec(root.right)}"
        
    return preOrderStr

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    out = preOrderRec(root)
    
    print(out)
    



tree = BinarySearchTree()

arr = [1, 2, 5, 3, 6, 4]
t = len(arr)

for i in range(t):
    tree.create(arr[i])


preOrder(tree.root)