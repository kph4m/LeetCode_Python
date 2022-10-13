"""
Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Understand

    1
  2   3
 4 5 6 7

- return [1,3,7]

    1
  2   3
 4 5 

- return [1,3,5]

- binary tree = left isn't less, right isn't greater
- just root?
    - return root
- what is the input structure like?
    - node with val, left, and right attributes

Match
- BFS, want to find the right-most value in each level

Plan
- perform bfs
- create output
- create queue
- while queue exists
    - go through each level and append left and right child
    - append the last value of the level to output
- return output

Implement

Review

    1
  2   3
 4 5 

queue = [1]
lastVal = 1
output = [1]

queue = [2,3]
lastVal = 2
queue = [3,4,5]
queue = [4,5]
lastVal = 3
output = [1,3]

queue = [5]
lastVal = 4
queue = []
lastVal = 5
output = [1,3,5]

Evaluate
- Time Complexity: O(n) - goes through each node in the tree once
- Space Complexity: O(n) - queue could have up to n nodes in the worse case
"""
from collections import deque

def rightSideView(root):
    if not root:
        return []

    output = []
    queue = deque()

    queue.append(root)

    while queue:
        # keep track of last val
        lastVal = 0

        # loop through all nodes in a level
        for i in range(len(queue)):
            node = queue.popleft()
            if not node:
                continue
            lastVal = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        output.append(lastVal)

    return output


    

    

    