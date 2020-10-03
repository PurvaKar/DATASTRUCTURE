"""
Recursion based Postorder Traversal of a tree
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
        
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end = " ")
    
    
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(8)
root.right.left = Node(2)
root.right.left.left = Node(1)
root.right.left.right = Node(12)
root.right.right = Node(7)

Postorder(root)