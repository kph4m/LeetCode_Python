"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Understand
- given root, return array of arrays by level order 
- root = 3, tree = [3,9,20,null,null,15,7]
    - [[3], [9,20], [15,7]]
- root = 1, tree = [1,2,3,4,5,6,7]
    - [[1], [2,3], [4,5,6,7]

Match
- BFS 

Plan
- create res array
- create q
- append root to q
- while q exists
    - create level array that will store levels to be pushed onto res
    - for i in range(level.length)
        - pop value
        - if it's not null
            - append the value to level
            - append the children to the queue
    - if level exists:
        - append it to res
- return res

Implement

Review
root = 3, tree = [3,9,20,null,null,15,7]
q = [3], level = [], qLen = 1
q =  [9,20], level = [3], res = [[3]], qLen=2
q = [20, null, null], level = [9]
q = [null, null, 15, 7], level = [9,20], res = [[3], [9,20]], qLen = 4
q = [null, 15, 7]
q = [15,7]
q = [7, null, null], level = [15]
q = [null, null, null, null], level = [7,15], res = [[3], [9,20], [7,15]], q = 4
q = [null, null, null]
q = [null, null]
q = [null]
q = [], level= []
return res = [[3], [9,20], [7,15]]


Evaluate
Time Complexity: O(n) - going through each node single time
Space Complexity: O(n/2) -> O(n) - queue could have biggest level of tree n/2
"""

from collections import deque
def levelOrder(root):

    if not root:
        return []
    
    res = []

    q = deque()

    q.append(root)

    while q:
        qLen = len(q)
        level = []

        # go through each element
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)

    return res



    

