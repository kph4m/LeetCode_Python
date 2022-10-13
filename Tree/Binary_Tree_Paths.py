"""
Binary Tree 

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Understand
- return all root to leaf paths
    - leaf = no left or right child

  1
 2 3
4

["1->2->4", "1->3"]

- empty?
    - return none
- no children?
    - return root only

Match
- DFS, Binary Tree

Plan
- in main function, create list that will contains all paths
- call the helper function
- return all_paths
- create helper function that will add paths (root, local_path, all_paths)
    - if root doesn't exist return
    - append to local path
    - if its a child, append the local path to all paths
    - recursive call on left and right child
    - as it returns up the tree, pop the value

Implement

Review

    1
   2 3
  4

local_path = "1"
 - local_path = "1","2"
    - local_path = "1","2", "4"
        - 4 is a leaf, append 1->2->4 to all_paths
        - pop 4 from local path
    - right child doesnt exist
 - pop 2 from local path 
 - local_path = "1", "3"
    - 3 is a leaf, append 1->3 to all paths
    - pop 3 from local path

Evaluate
- Time Complexity: O(n) - visit all nodes in tree once
- Space Complexity: O(n) - recursion stack

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binaryTreePaths(root):
    all_paths = []

    def dfs(root, local_path, all_paths):

        if not root:
            return
        
        # append node to local path
        local_path.append(str(root.val))

        # if leaf node, path ends, add it to all path
        if not root.left and not root.right:
            all_paths.append("->".join(local_path))
        
        # recursive calls on left and right child
        dfs(root.left, local_path, all_paths)
        dfs(root.right, local_path, all_paths)

        # remove node as we return back to up the tree to explore new paths
        local_path.pop()
    dfs(root, [], all_paths)

    return all_paths

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)


root3 = Node(1)
root3.left = Node(2)
root3.right = Node(3)
root3.left.left = Node(4)


print("Expected Output: ['1->2', '1->3']")
print("Actual Output: ", binaryTreePaths(root))

print("Expected Output: ['1->2->3']")
print("Actual Output: ", binaryTreePaths(root2))

print("Expected Output: ['1->2->4', '1->3']")
print("Actual Output: ", binaryTreePaths(root3))
