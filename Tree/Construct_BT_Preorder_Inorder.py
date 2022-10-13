"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,  construct and return the binary tree.

Understand
    1
  2   3
 4 5 6 7
- preorder -> 1,2,3,4,5,6,7
- inorder -> 4,2,5,1,6,3,7
- construct a binary tree based on these arrays of preorder and inorder

Match
- Preorder, Inorder

Plan
- preorder is top to bottom, we'll use it to construct the tree
- inorder is left to right, we'll use it to partition left and right values

Implement

Review
    3
  9   20
     15 7
- preorder -> 3,9,20,15,7
- inorder -> 9,3,15,20,7


root = 3
root.left: preorder = [9,20,15,7], inorder = [9]
    - root = 9
    - root.left: preorder = [20,15,7], inorder = []
        - inorder empty
    - root.right: preorder = [20,15,7], inorder = []
        - inorder empty
    - return 9
root.right: preorder = [20,15,7], inorder = 15,20,7
    - root = 20
    - root.left: preorder = [15,7], inorder = [15]
        - root = 15
        - root.left: preorder = [7], inorder = []
            - inorder empty
        - root.right: preorder = [7], inorder = []
            - inorder empty
        - return 15
    - root.right: preorder = [7], inorder = [7]
        - root = 7
        - root.left: preorder = [], inorder = []
            - inorder empty
        - root.right: preorder = [], inorder = []
            - inorder empty
        - return 7
    - return 20
- return 3

Evaluate
- Time Complexity: O(n^2) - go through each node in the tree, pop is O(n)
- Space Complexity: O(1) - no data structure used
"""
from collections import deque

# Time Complexity: O(n^2) - going through each node, pop is O(n)
# Space Complexity: O(1) - no data structure used
def buildTree(preorder, inorder):
    if inorder:
        # get ind of the popped preorder value
        ind = inorder.index(preorder.pop(0))

        # create node out of the value of ind
        root = TreeNode(inorder[ind])

        # set left
        root.left = buildTree(preorder, inorder[0:ind]) 

        # set right
        root.right = buildTree(preorder, inorder[ind+1:])

        return root

# # Optimized using deque for preorder (O(1) for pop)
# def buildTree(preorder, inorder):
#     preorder = deque(preorder)

#     def getTree(preorder,inorder):
#         if inorder:
#             # get ind of the popped preorder value
#             ind = inorder.index(preorder.popleft())

#             # create node out of the value of ind
#             root = TreeNode(inorder[ind])

#             # set left
#             root.left = buildTree(preorder, inorder[0:ind]) 

#             # set right
#             root.right = buildTree(preorder, inorder[ind+1:])

#             return root
            
#     return getTree(preorder, inorder)

    