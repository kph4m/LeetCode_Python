"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Understand
- each house has certain money stashed
- constraint: adjacent houses have securtiy systems connected, can't rob two adjacent houses on the same night
- [3,5,6,2,3,4]
    - 3 + 6 + 3 = 12
- no negatives
- if just 1 element
    - return nums[0]

Match
- Dynamic Programming

Plan
[rob1, rob2, n]
rob2 = current max profit as we traverse the list
rob1 = stores the previous max profit so we can compare as we traverse

iterate through list
    - find max
    - set rob1 to prev max
    - set rob2 to new max
by the end, rob2 should store the max profit

Implement

Review
[2,3,5]
n = 2
temp = max(2,0)
        = 2
rob1 = 0
rob2 = 2

n = 3
temp = max(3,2)
rob1 = 2
rob2 = 3

n = 5
temp = max(7,3)
rob1 = 3
rob2 = 7

return 7

[4,2,1,5]
[rob1, rob2, n, n+1]

n = 4
temp = 4
rob1 = 0
rob2 = 4

n = 2
temp = 4
rob1 = 4
rob2 = 4

n = 1
temp = 5
rob1 = 4
rob2 = 5

n = 5
temp = 9
rob1 = 5
rob2 = 9

Evaluate
"""
def rob(nums):
    # Approach 1
    # if not nums:
    #     return 0

    # if len(nums) < 2:
    #     return max(nums)

    # else:
    #     rob1, rob2 = 0,0
    #     for n in nums:
    #         # get max 
    #         temp = max(rob1 + n, rob2)
    #         rob1 = rob2
    #         rob2 = temp
    #     return rob2

    
    # Approach 2
    if not nums:
        return 0

    if len(nums) < 2:
        return max(nums)

    # Create dp array where each position represents the max up to that point
    dp = [0] * len(nums)

    # First house
    dp[0] = nums[0]

    # Second house - find max between first and second house
    dp[1] = max(nums[0], nums[1])

    # iterate through nums starting at 3rd house
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    return dp[-1]

print("Expected Output: 7")
print("Actual Output: ", rob([2,3,5]))


print("Expected Output: 12")
print("Actual Output: ", rob([2,7,9,3,1]))

print("Expected Output: 9")
print("Actual Output: ", rob([4,1,2,5]))