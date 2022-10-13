"""
Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Understand
- given root, return kth smallest


     5
   4  8
  1  6

return 3rd smallest -> 5

- can there be duplicates? nah
- what if k is greater than the number of nodes in the bst?
    - return none
    - how to check number of nodes initially?
        - cant without traversing tree, skip check

Match
- Depth first search (Inorder), Stack

Plan
- go all the way to the left, adding all nodes to the stack
- reassign root to the pop stack value
- subtract k
- if k doesn't exist anymore, return root.val
- else, assign root to right child

Implement

Review 

     5
   4  8
  1  6

return 5th smallest

[5,4,1]
[5,4]
root = 1
k = 4
root = 1.right
Doesn't exist
[5]
root = 4
k = 3
root = 4.right
Doesn't exist
[]
root = 5
k = 2
root = 5.right = 8
[8,6]
[8]
root = 6
k = 1
root = 6.right 
Doesn't exist
[]
root = 8
k = 0, return 8


Evaluate
- Time Complexity: O(H+k), where H is the tree height
- Space Complexity: O(n), worse case is a skewed tree

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(4)
root.left.left = Node(1)
root.right = Node(8)
root.right.left = Node(6)

def kthSmallest(root, k):

    # Iterative Approach
    # stack = []
    # while True:
    #     # go all the way to the left for each node
    #     while root:
    #         stack.append(root)    
    #         root = root.left

    #     root = stack.pop()
    #     k -= 1
    #     if not k:
    #         return root.val
    #     root = root.right

    # Recursive Approach
    arr = []
    count = 0
    def inorder(root,arr,count):
        if root:
            inorder(root.left,arr,count)
            arr.append(root.val)
            inorder(root.right,arr,count)
        return arr
    return inorder(root,arr,count)[k-1]

print("Expected Output: 8")
print("Actual Output: ",kthSmallest(root, 5))