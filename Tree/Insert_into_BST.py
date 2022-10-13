"""
Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


Understand
- BST 
    - Left values < node < right value
- return root node after insertion
- new values don't exist in original bst
    - don't need to worry about duplicates
- what if no root?
    - set new value as root and return it


Match
- DFS, BST

Plan
- if no root
    - set new value as root and return
- if val < root
    - root.left = recursive call(root.left,newVal)
- if val > root
    - root.right = recursive call(root.right, newVal)
- return root

Implement

Review

Insert 4
   1
  2 3

root = 1
    - 1 < 4, move right
        - 3 < 4, move right
            - 3.right none, return TreeNode(4) 
            - return to previous recursive call, 3.right = TreeNode(4)
- return TreeNode(1)


Evaluate
- Time Complexity: O(n) - unbalanced worse case, have to visit all nodes
- Space Complexity: O(n) - recursion stack


"""

def insertIntoBST(root, val):

    # if root doesn't exist, return the node with val
    if not root:
        return TreeNode(val)

    # if val less than root, go left
    if val < root.val:
        root.left = insertIntoBST(root.left,val)
        
    # if val greater than root, go right
    if val > root.val:
        root.right = insertIntoBST(root.right,val)

    # should've been inserted by this step, return root
    return root