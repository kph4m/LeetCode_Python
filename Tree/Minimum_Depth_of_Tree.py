"""
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Understand
- find the minimum depth of a binary tree
- minimum depth = number of nodes along the shortest path from the root node down to the nearest leaf node
 
       3
      / \
      9  20
        /  \ 
       15   7

- return 2, 3 -> 9

Match
- recursion or iterative

Plan
- recursive
    - traverse tree and find the depth of left and right subtrees
    - return the minimum of the two + 1 for the root
- iterative
    - use a queue to traverse the tree
    - root and level to queue
    - first node that has no children is the minimum depth

Implement

Review

Evaluate
"""
# Recursive
# Time Complexity: O(n), go through all nodes
# Space Complexity: O(n) because of the recursive calls
def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1 + minDepth(root.right)
    if root.right is None:
        return 1 + minDepth(root.left)
    # get the minimum depth of the left and right subtrees + 1 for the root
    return 1 + min(minDepth(root.left), minDepth(root.right))

# Deque
# Time Complexiy: O(n), go through all nodes
# Space Complexity: O(n) because of the queue
import collections
def minDepth(root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print("Expected Output: 2")
print("Actual Output:", minDepth(tree))