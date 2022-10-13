"""
Lowest Common Ancestor of Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Understand
- Return the lowest common ancestor of two nodes
- Node can be a descendant of itself
    - [2,4], p = 2, 4 = q, ancestor is 2

Match
- Binary Search Tree

Plan    
- create pointer to keep track of current node
- keep traversing tree while cur isn't null
    - if both nodes are less than the current node, move to the left
    - if both nodes are more than the current node, move to the right
    - else
        - one node could be greater than and one node could be less than current node
        - one node could equal the current node
        - whatever the case, return the current node as thats the common ancestor of both of them

Implement

Review
- root = [6,2,8,0,4,7,9,null,null,3,5], p = 4, q = 5
- 4,5 < 6, cur = 2
- 4,5 > 2, cur = 4
- return 4

Evaluate
- Time Complexity: O(logn) - visiting only one node per level
- Space Complexity: O(1) - not creating any new data structs
"""

def lowestCommonAncestor(root, p, q):

    # check input
    if not root or not p or not q:
        return None

    # start at root
    cur = root

    while cur:
        # if cur lower than both nodes, move to right
        if cur.val < p.val and cur.val < q.val:
            cur = cur.right
        # if cur greater than both nodes, move to left
        elif cur.val > p.val and cur.val > q.val:
            cur = cur.left
        else:
            return cur

