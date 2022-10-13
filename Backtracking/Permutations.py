"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Understand
- given array with distinct integers, return all permutations
- [1,2,3]
    - [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
Match
- Backtracking, DFS

Plan
- create res to store permutation
- create back track algo
    - stopping condition: if len of constructed permutation == len of nums, append to res, return
    - else, iterate through all nums in num:
        - if num is already in the constructed permutation, skip it
        - else, add it to the permutation
        - call dfs on new constructed permutation
        - after it finished constructing it, remove it from the set
- call backtrack algo
- return res

Implement

Review

Evaluate
- Time Complexity: O(n * n!) - going through each nums and getting the permutations
- Space Complexity: O(n) - recursion depth
"""

def permutate(nums):

    # store permutations
    res = []

    # acc = constructing the permutation
    def dfs(acc):

        # if len of the constructed permutation == len of nums, we stop and append it to res
        if len(acc) == len(nums):
            res.append(acc.copy())
            return
        
        # if not finished constructing the permutation, keep building it by iterating through the nums
        for num in nums:     
            # if num is already in the permutation, skip it 
            if num in set(acc): 
                continue  

            # append num to permutation
            acc.append(num)

            # dfs on permutation
            dfs(acc)

            print(acc)

            # can't build any more solutions using current num, remove it 
            acc.pop()                   
    dfs([])
    return res

print("Expected Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]")
print("Actual Output: ", permutate([1,2,3]))