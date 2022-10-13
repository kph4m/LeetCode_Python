"""
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Understand
- check all subtrees of a node to make sure their heights don't differ more than 1

Match
- Binary Tree

Plan
- start from bottom of tree
- get height of left and right subtrees in constant time and if its balanced
- check if difference isn't more than 1

Implement

Review

Evaluate
- Time Complexity: O(n) - going through all nodes in tree
- Space Complexity: O(h), where h is the height of the tree
"""

def isBalanced(root):
    
    # dfs
    def dfs(root):
        
        # base case - is balanced, height of 0
        if not root: 
            return [True, 0]

        # get left and right balance boolean and height
        left, right = dfs(root.left), dfs(root.right)

        # check if balanced
        # difference in height between subtrees isn't greater than 1
        # left and right subtrees are balanced
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <=1)

        # return balanced value and 1 + max(height of left, height of right)
        return [balanced, 1+max(left[1], right[1])]

    # return boolean value
    return dfs(root)[0]