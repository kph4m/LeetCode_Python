"""
Unique Binary Search Tress

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Understand
- bst = left < root < right
- n=3
    1
    \
     2
    /
   3

    1
     \
      3
     /
    2

    2
   / \
  1   3

     3
    /
   2
  /
 1

    3
   / \
  1   2

- consider each number as the root
- the left subtree will be the numbers less than the root
- the right subtree will be the numbers greater than the root
- the total number of trees will be the product of the left and right subtrees

1 2 3
1 as root = 1 (left) * 2 (right) = 2
2 as root = 1 (left) * 1 (right) = 1
3 as root = 2 (left) * 1 (right) = 2

strat: use dp to store the total number of trees for each number as a root

OR

- cheat and use the formula to get the total number of trees
- (2n)! / (n+1)!n!

Match
- recursion

Plan
DP
- create a helper function that takes in a start and end
    - create dict to store the total number of trees for each number as a root
    - get the total number of trees for each number as a root

Formula
- create a helper function for factorial and use the formula

Implement

Review

Evaluate
"""
# DP
# Time Complexity: O(n^2) because of the for loop and the recursive calls
# Space Complexity: O(n) because of the memo
def numTrees(n):
    memo = {}
    def helper(start, end):
        # base case
        if start >= end:
            return 1
        total = 0
        # check if the start and end are in the memo because we don't want to repeat calculations
        if (start, end) in memo:
            return memo[(start, end)]
        # 
        else:
            for i in range(start, end + 1):
                # recursively call the helper function for subtrees and get the total when a value is a root
                total += helper(start, i - 1) * helper(i + 1, end)
            memo[(start, end)] = total
            return total
    return helper(1, n)

# Using the formula
# Time Complexity: O(n) because of the factorial
# Space Complexity: O(1) because no data structures are used
def numTrees(n):
    def factorial(n):
        total = 1
        for i in range(1, n+1):
            total *= i
        return total
    
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))

print("Expected Output: 5")
print("Actual Output:", numTrees(3))

print("Expected Output: 1")
print("Actual Output:", numTrees(1))

print("Expected Output: 2")
print("Actual Output:", numTrees(2))