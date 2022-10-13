"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Understand
- given root, check if its binary search tree
    - left subtree less than nodes key
    - right subtree more than nodes key
    - left and right subtree must be bst as well
    -  5
     /  \
    2    7
   / \  / \
   1  3 6  8

- create left and right bounds
    - if all nodes are within these bounds, its valid

Match
- DFS / BFS

Plan
- create recursive function (node, left, right)
    - true condition: if it reaches a leaf, return true
    - false condition: if its not within the bounds, return false
    - recursive call
- recursive call(root, -inf, inf)

Implement

Review
-      5
     /  \
    1    4
        / \
        3  6

5
- 1
    -inf < 1 < 5
    - leaf
        - return True
    - leaf
        - return true
    - return True
- 4
    - 5 < 4 < inf = False
    - return False
- return False

Evaluate
- Time Complexity: O(n) - visit each node once
- Space Complexity: O(n) - recursion
- 
"""

def isValidBST(root):

    def valid(node, left, right):
        # if reaches leaf, all prev nodes valid
        if not node:
            return True
        # Return false if not within bounds
        if not node.val < right and not node.val > left:
            return False
    
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
    return valid(root, float('-inf'), float('inf'))
