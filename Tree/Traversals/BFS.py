#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:27:28 2020

@author: anishukla
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
        
def TreeBFS(root):
    q = [root]
    L = []
    while len(q) != 0:
        A = q.pop(0)
        L.append(A.data)
        if A.left:
            q.append(A.left)
        if A.right:
            q.append(A.right)
        
    return L
        
    
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(8)
root.right.left = Node(2)
root.right.left.left = Node(1)
root.right.left.right = Node(12)
root.right.right = Node(7)

TreeBFS(root)