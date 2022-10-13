"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Understand
- given binary tree and p q, find the lowest common ancestor of p and q
- since it's a binary tree, it won't be sorted left < root and right > root
- [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    - path to 5: 3->5
    - path to 4: 3->5->2->4
	- return 5

Match 
- DFS to traverse the tree

Plan
- traverse tree for p and q
    - if p and q are in different subtrees, their values will return to the common ancestor (first not null return)
    - if p ancestor of q, just return p
    - if q ancestor of p, just return q

- recursive function
    - escape condition: if no root or root == p or root == q
    - search left and right subtree
    - if left and right values exist, then the values are found within the root subtree,
    return root
    - if one valid value but one null value returned, just return the valid value

Implement

Review
[0,1,2,3,4,5,6], p = 4, q=6

0 
    - 1
        - 3 (left)
            - leaf
                - return null
            - leaf
                - return null
            - return null
        - 4 (right)
            - root = p
            - return 4
        - return 4
    - 2
        - 5 (left)
            - leaf
                - return null
            - leaf
                - return null
            - return null
        - 6 (right)
            - root = q
            - return 6
        - return 6
    - return 0

Evaluate
- Time Complexity: O(n) - visit all nodes in tree
- Space Complexity: O(n) - max amount of space utilized by recursion stack

"""

def lowestCommonAncestor(self,root,p,q):

    # escape condition
    if not root or root == p or root == q:
        return root

    # search left
    left = self.lowestCommonAncestor(root.left,p,q)

    # search right
    right = self.lowestCommonAncestor(root.right,p,q)

    # if left and right values exists, return root
    if left and right:
        return root

    # if only one valid value, return the valid value
    if left and not right:
        return left

    if right and not left:
        return right