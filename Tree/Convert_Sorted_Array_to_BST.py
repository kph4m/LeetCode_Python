"""
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Understand
- given ascending sorted array, convert it to a height-balanced binary search tree
- BST - left node is less than the parent node, right node is greater than the parent node
- height-balanced - the depth of the two subtrees of every node never differs by more than one
- return root

nums = [-10,-3,0,5,9]
output = [0,-3,9,-10,null,5]

- empty?
    - return none
- 1 node?
    - return nums[0]
- any duplicates?
    - no

Match
- Left, Right, Middle (root for each subtree) Pointers 

Plan
  • Because it's a sorted array, we can assign the middle element 
    as the root. (Middle here is index len(nums//2)); the elements 
    to the left of the root element comprise the left subtree,
    and the elements to its right comprise the right
    subtree. For example, let:
 
          nums = [1,4,5,6, _8_, 9,10,11,14] ; len(nums) == 9
 
    Tthe middle element is nums[9//2] = nums[4]= 8, so the left 
     subtree is [1,4,5 6] and the right subtree is [9,10,11,14] 
                        
                      ____8____
                     /         \
            [1,4,_5_,6]        [9,10,_11_,14]
 
  • Next we repeat the process for the subtree of the left and
.    right subtrees:

                       ______8______             
                    /                \
                   5                  11
                  / \                /   \
     [1,_4_, None]  [6]  [9,_10_, None]   [14]

  • We continue on recursively until the subtrees are completed.

                             __8_____
                            /        \
                           5         _11
                          / \       /   \
                         4   6     10    14
                        /         /
                       1         9


- helper(left,right)
    - if right is less than left
        - return nothing
    - calculate mid point
    - initiate root node using midpoint value
    - midpoint.left = helper(left, mid - 1) - recurse on the left side of the mid
    - midpoint.right = helper(mid + 1, right) - recurse on the right side of the mid
    - return root

Implement

Review
[-10,-3,0,5,9]
0
 - left: -3
    - left: -10
 - right: 9
    - left: 5


Evaluate
- Time Complexity: O(n), traversing every element in the input array
- Space Complexity: O(n), creating a new node for each element in the input array
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):

    def helper(left,right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)
        return root

    return helper(0,len(nums)-1)

print("Expected Output: 0")
print("Actual Output: ", sortedArrayToBST([-10,-3,0,5,9]).val)
print("Expected Output: 1")
print("Actual Output: ", sortedArrayToBST([1,3]).val)