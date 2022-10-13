"""
Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Understand
[4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
[1,4,7,2,5] -> [1,7,4,5,2]
subtrees are inverted, root remains the same

Match
Trees traversal using left and right children, dfs

Plan
if no root, return none
switch values of left and right children
perform recursive call to left and right children
return root

Implement 

Review
[1,4,7,2,5] 
1 exists
swap 4 and 7 -> [1,7,4]
4 exists, doesn't have children so stops
7 exists, swaps 2 and 5 -> [1,7,4,5,2]
2 exists, doesn't have children so stops
5 exists, doesn't have children so stops
final binary tree = [1,7,4,5,2], return 1

Evaluate
Time Complexity: Traverse each node in the tree once. O(n), where is n is the total nodes in the tree
Space Complexity: Each recursive function call will be stored on program stack. O(h), where h is the height of the tree.
"""

def invertTree(root):

    # check if root exists
    if not root:
        return None
    
    # swap left and right children
    temp = root.right
    root.right = root.left
    root.left = temp

    # recursive calls
    invertTree(root.right)
    invertTree(root.left)

    # return root after all swaps
    return root