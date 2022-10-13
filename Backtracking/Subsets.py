"""
Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Understand
- given integer array with unique elements, return all possible subsets (power set - all possible combinations of all possible lengths, from 0 to n)
- can't contain duplicate subsets
- return solution in any order
- [1,2] -> [[], [1], [2], [1,2]]

Match
- Backtracking

Plan

Iterative Approach
add each individual element to subsets found

[1,2,3]

1:
[[]]
[[], [1]]

2: Append 2 to all subsets
[[], [1], [2]]
[[], [1], [2], [1,2]]

3: Append 3 to all subsets
[[], [1], [2], [1,2], [3]]
[[], [1], [2], [1,2], [3], [1,3]
[[], [1], [2], [1,2], [3], [1,3], [2,3]]
[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

- create output array with empty subset already in it
- iterate through all elements in nums
 - for i in range(len(subset)):
    - append current subset to subset + element
- return subset



Backtracking approach
generate all possible combinations for a given length

[1,2,3]

length 0: []
length 1: [1], [2], [3]
length 2: [1,2], [1,3], [2,3]
- assign 1 as first element
    - subsets complete
- assign 2 as first element
    - subsets complete
length: 3: [1,2,3]


Back Track Approach
- backtracking psuedocode (first element, combination)
    - if current combination done, add combination to final output
    - else, iterate over indexes from first to length of entire sequence n
        - add integer nums[i] to current combination curr
        - recurse and add more integer into the combination using the next element
        - backtrack by removing nums[i] from curr
Implement

Review
[1,2,3]

1:
[[]]
[[], [1]]

2: Append 2 to all subsets
[[], [1], [2]]
[[], [1], [2], [1,2]]

3: Append 3 to all subsets
[[], [1], [2], [1,2], [3]]
[[], [1], [2], [1,2], [3], [1,3]
[[], [1], [2], [1,2], [3], [1,3], [2,3]]
[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Evaluate
Time Complexity: O(n * 2^n) - 2^n (number of subsets), subsets can be of length n 
Space Complexity: O(n) - subsets array to return
"""

def subsets(nums):

# # BackTrack Approach
#     def backtrack(first, combs):
#         # exit condition: if length == subset length
#         if len(combs) == k:
#             output.append(combs[:])
#             return

#         # iterate through
#         for i in range(first, n):
#             # add to current combination
#             combs.append(nums[i])

#             # recurse on next elements
#             backtrack(first, combs)

#             # backtrack
#             combs.pop()

#     output = []
#     n = len(nums)

#     first = 0
#     combs = []

#     # iterate through all subset lengths
#     for k in range(n+1):
#         backtrack(first, combs)

#     return output

# Iterative Approach
    subsets = [[]]

    # iterate through all nums to add to each subset
    for num in nums:
        # iterate through all subsets to add num to it
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])

    return subsets

print("Expected Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]")
print("Actual Output: ", subsets([1,2,3]) )

print("Expected Output: [[]]")
print("Actual Output: ", subsets([]) )

print("Expected Output: [[], [0]]")
print("Actual Output: ", subsets([0]) )