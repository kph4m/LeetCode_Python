"""
Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Understand
- given root, return length of the diameter
    - diameter is the length of longest path between two node in a tree
    - length represented by number of edge between them
- [1,2,3,4,5]

        1
       / \
      2   3
     / \
    4   5

longest path are 4-2-1-3, 5-2-1-3 = 3 edges

Match
- Trees

Plan
- calculate the height from the left and right tree using dfs
- calculate the diameter, which will be height of left + right tree

Implement

Review
[1,2,3,4,5]
- root = 1, left = 2, right = 3
    - root = 2, left = 4, right = 5
        - root = 4
            - 4.left = return 0
            - 4.right = return 0
            - diameter = 0
            - return 1
        - root = 5
            - 5.left = return 0
            - 5.right = return 0
            - diameter = 0
            - return 1
        - diameter = 1
        - return 2
    - root = 3
        - 3.left = return 0
        - 3.right = return 0
        - diameter = 0
        - return 1
    - diameter = 3
    - return 4
- return 3

Evaluate
- Time Complexity: O(n) - go through each node in the tree
- Space Complexity: O(n) - recursion stack
"""

def diameterOfBinaryTree(root):

    def dfs(root):
        # nonlocal - work with variables inside nested functions
        # without it, it'll return the global diameter variable
        nonlocal diameter

        # if theres no root, then the height running through the root node is 0
        if not root:
            return 0

        # recursive calls on left and right
        left = dfs(root.left)
        right = dfs(root.right)

        # update diameter to max value
        diameter = max(left+right, diameter)

        # return the height running through the root node
        return 1 + max(left,right)
        
    diameter = 0
    dfs(root)
    return diameter

