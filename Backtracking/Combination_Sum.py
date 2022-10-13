"""
Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Understand
- given candidates (array of distinct integers) and target, return list of list that has all combinations of numbers that sum up to target
- same number can be chosen unlimited number of times
    - [2,3,6,7], 7
    - [[2,2,3],[7]]

Match
- DFS to go through each combination

Plan
- exhaust the duplicates until it cant fit target anymore
    - [2,3,5], targ = 8
        - [2]
        - [2,2]
        - [2,2,2]
        - [2,2,2,2], reached targ or exceeded targ
        - goes back up to find combinations using duplicates
        - after it find all the combinations using all numbers, remove 2 from possible combinations, finds all combinations using 3 and 5
- keep removing duplicates and test the next values in the array 


- create res to store the results in
- create DFS function with 3 params
    - i to iterate through nums
    - cur to keep track of combinations
    - total for the sum of the combinations
    - Base cases
        - if total == target
            - append cur to result
        - if total > target or i goes out of bounds
            - return
    - append current i value to cur
    - call dfs on the current i value
        - will check every combination with duplicate i values
    - pop it from cur, we don't want to check combinations with i anymore
    - call dfs on the next i value
- return res

Implement

Review

Evalaute
- Time Complexity: O(2^n) - each node has two decisions
- Space Complexity: O(n*n)? - recursion and copy of list
"""
def combinationSum(candidates, target):

    res = []

    def dfs(i, cur, total):

        # Base Cases

        # if total matches target, append to res list
        if total == target:
            res.append(cur.copy())
            return

        # if i exceeds len of nums or total > target, return
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])

        # combinations with duplicate i values
        # when it returns, it reached or exceeded the target value with duplicates
        dfs(i, cur, total + candidates[i])

        cur.pop()
        # remove one value and test combinations with next values in candidates array
        dfs(i + 1, cur, total)

    dfs(0,[],0)
    return res


print("Expected Output: [[2,2,3],[7]]")
print("Actual Output: ", combinationSum([2,3,6,7],7))

print("Expected Output: [[2,2,2,2],[2,3,3],[3,5]]")
print("Actual Output: ", combinationSum([2,3,5],8))