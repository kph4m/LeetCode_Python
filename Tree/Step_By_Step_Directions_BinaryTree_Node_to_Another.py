"""
Step by Step Directions from a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.


Understand
- given start and end node, get the path from start to end
- 'U' = go from node to parent
- 'L' = parent node to left child
- 'R' = parent node to right child
- [5,1,2,3,null,6,4], startValue = 4, endValue = 3
    - 'UULL'
- [1,2], startValue = 2, endValue=1
    - 'U'
- startValue = endValue?
    - no
- will startValue and endValue always exist in the graph
    - yes
- only one node?
    - no path

Match
- Graph, BFS

Plan
- Create Graph (dictionary) that contains the connections for all the nodes using bfs
    - {5: [(1,'L'), (2,'R')], 1: [(5, 'U')], 2: [(5,'R')]}
- Go through graph using bfs(), queue will contain (node,"path")
    - Create visited set so don't encounter a cycle
    - when reaches endvalue, return path

Implement

Review
[1,2,3], start = 1, end = 3

Create Graph
graph = {1: [(2,'U')], 2: [(1,'L'), (3,'R')], 3: [(2,'U')]}

queue = [(1,"")]
visited = {1}
queue = [(2,"U")]

visited = {1,2,3}
queue = [(3,'UR')]

val = destVal, return 'UR'

Evaluate
"""
from collections import defaultdict, deque
from turtle import left, right

def getDirections(root, startValue, destValue):
    if not root or not startValue or not destValue:
        return ""

    # Create Graph
    graph = defaultdict(list)

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left:
            graph[node.val].append((node.left.val, 'L'))
            graph[node.left.val].append((node.val, 'U'))

            queue.append(node.left)

        if node.right:
            graph[node.val].append((node.right.val, 'R'))
            graph[node.right.val].append((node.val, 'U'))
            queue.append(node.right)

    # BFS on graph
    queue2 = deque([(startValue, "")])

    # set to prevent cycle
    visited = set()

    while queue2:
        val, path = queue2.popleft()

        if val in visited:
            continue

        visited.add(val)

        if val == destValue:
            return path
        
        else:
            for node, direction in graph[val]:
                if node not in visited:
                    queue2.append((node, path+direction))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(1)

print("Expected Output: UR")
print("Actual Output: ", getDirections(root, 1,3))