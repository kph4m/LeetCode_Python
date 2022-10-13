"""
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Understanding
- given array with positive nums, determine if array can be split into two subsets where the sums are the same value
- [1,5,11,5] -> [1,5,5], [11] = True
- is it always possible for it to be partitioned?
    - need to check if its even first to even think about partitioning it
- the target value for each partiion can be determined by sum(nums) // 2 since they need to be equal


Match
- Dynamic Programming

Plan
- calculate target: sum(nums) // 2
- calculate all combinations for the input and store it in a set
- if target is found within that set, then its possible to split the nums into partitions so return true
    - else return false

Implement

Review
[1,5,11,5]

22 % 2 = 0, can partition
target = 22 / 2 = 11

dp = {0}
i = 1
dp = {0, 1}
i = 5
dp = {0,1,5,6}
i = 11
dp = {0,1,5,6,11}
target calculated, return True


Evaluate
- Time Complexity: O(n) - first for loop, O(n) - copy, O(len(dp), upperbound can be sum(nums)) - second for loop, O(n * sum(nums))
- Space Complexity: O(n) - creating a new set of n elements for each iteration

"""

def canPartition(nums):

    # check if its possible to partition
    if sum(nums) % 2:
        return False

    # create the set for storing the combinations
    dp = set()
    dp.add(0)

    # target that we want to look for in the combinations
    target = sum(nums) // 2

    # iterate through each element in nums
    for i in range(len(nums)):
        newDp = dp.copy()
        # iterate through each element in dp
        for total in dp:
            # if target is calculated, return True
            if (total + nums[i] == target): 
                return True
            else:
                if (total + nums[i] <= target):
                    newDp.add(total + nums[i])
            
        print(dp)
        dp = newDp

    print(dp)

    return False


print("Expected Output: True")
print(canPartition([1,5,11,5]))


print("Expected Output: False")
print(canPartition([1,2,3,5]))