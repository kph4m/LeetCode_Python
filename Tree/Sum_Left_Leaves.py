"""
Sum of Left Leaves in Binary Tree

Understand
- given binary tree, return sum of all left leaves

   1
 2  3
6  4

6 + 4 = 10

- what if there's no left leaves?
        - return 0
- no root?
        - return 0
    
        
Match
- DFS iterative, Binary Tree

Plan
- create sum variable
- create stack where each value has the node and a boolean that determines if its a left or right node
- while stack exists
        - pop the first value
        - if it doesn't exist, continue
        - if its a leaf
            - if its a left node
                - add it to result
        - else, add neighbors to stack and continue
- return the result

Implement

Review

Evaluate
- Time Complexity: O(n) - going through all nodes in the tree
- Space Complexity: O(n) - stack
"""

def sum_of_left_leaves(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    leftLeafSum = 0
    
    stack = [(root, False)]
    
    while stack:
        cur, isLeft = stack.pop()
        
        if not cur:
            continue
        
        # if its a leaf
        if not cur.left and not cur.right:
            if isLeft:
                leftLeafSum += cur.val
                
        else:
            stack.append((cur.left, True))
            stack.append((cur.right, False))
                
    return leftLeafSum