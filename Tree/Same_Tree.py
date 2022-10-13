"""
Same Tree 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Understand
- same = structured identically and nodes have same value
- [1,2,3] = [1,2,3]
- [1,3,2] !- [1,2,3]

Match
- Binary Tree, DFS

Plan
- traverse both subtrees 
    - if they both reached leaf node, return true
    - if the nodes values aren't equal, return false
    - return recursive call

Implement

Review
p = [1,3,2], q = [1,2,3]

p = 1, q = 1, p = q
    - p.left = 3, q.left = 2
        - return False
    - p.right = 2, q.right = 3
        - return False

return False

Evaluate
- Time Complexity: O(n) - visit all nodes once
- Space Complexity: O(n) - recursion stack
"""

def isSameTree(self,p,q):

    # if its finished traversing and no difference, return true
    if not p and not q:
        return True
    
    # if one is empty and the other isn't, not the same
    if not p or not q:
        return False

    # if values aren't the same, return false
    if p.val != q.val:
        return False

    # recurse on the children
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
