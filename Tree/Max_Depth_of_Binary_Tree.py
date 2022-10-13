"""
Max Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Understand
- given root, return max depth (num of node from root to lower tree node)

        1
       / \
      2   3
         / \
        4   5
             \
              6

Longest path is 1->3->5->6, return 4

Match
- Binary Tree, DFS

Plan
- if root doesn't exist
    - return none
- use recursive dfs to go through each left and right elements and return the max of them
    - 1 + max(maxdepth(root.left), maxdepth(root.right))

Implement

Review
        1
       / \
      2   3
         / \
        4   5
             \
              6

- maxDepth(1)
    - maxDepth(2)
        - maxDepth(2.left)
            - return None
        - maxDepth(2.right)
            - return None
        - return 1
    - maxDepth(3)
        - maxDepth(4)
            - maxDepth(4.left)
                - return None
            - maxDepth(4.right)
                - return None
            - return 1
        - maxDepth(5)
            - maxDepth(6)
                - maxDepth(6.left)
                    - return None
                - maxDepth(6.right)
                    - return None
                - return 1
            - return 2
        - return 3
    - return 4


Evaluate
- Time Complexity: O(n), go through each node once
- Space Complexity: O(n), recursive stack

"""

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
