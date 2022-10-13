"""
Print Binary Tree

Given a binary tree, print all its leaf nodes from left to right


Understand
- print leaf nodes of a binary tree from left to right
    - Level order traversal
  1   
 2 3

2, 3

   1
    2
     3

3

- what if tree null?
    - don't print anything since no leaf nodes



Match
- Binary Tree, DFS

Plan
- if no root, return
- if no left and right child,
    - print(root.val, end=" ")
- recurse on left and rightr child

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printBinaryTree(self,root):
        if not root:
            return

        if not root.left and not root.right:
            print(root.val," ",end="")
        
        # recurse on left and right if they exist
        self.printBinaryTree(root.left) 
        self.printBinaryTree(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)

print("Expected Output: 2 3")
print("Actual Output: ")
root.printBinaryTree(root)

print("Expected Output: 3")
print("Actual Output: ")
root.printBinaryTree(root2)






