"""
Max Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.


Understand
- return the sum of the max subarray
- nums = [-2,1,-3,4,-1,2,1,-5,4], maxSubarray = 4,-1,2,1, sum = 6
- nums = [1], maxSubarray = 1, sum = 1
- nums = [5,4,-1,7,8], maxSubarray = 5,4,-1,7,8, sum = 23

Match
- List 

Plan
- check if nums is empty
- create variable for current sum
- create variable for max sum
- iterate through list
    - if adding the previous int contributed to a neg sum, reset current sum back to 0
    - add current int to current sum
    - set max sum to max(current sum, max sum)
- return max sum

Implement

Review
- nums = [-2,1,-3,4,-1,2,1,-5,4]
- maxSum = -2, curSum = 0
- curSum = -2, maxSum = -2 
- reset curSum = 1, maxSum = 1
- curSum = -2, maxSum = 1
- reset curSum = 4, maxSum = 4
- curSum = 3, maxSum = 4
- curSum = 5, maxSum = 5
- curSum = 6, maxSum = 6
- curSum = 1, maxSum = 6
- curSum = 5, maxSum = 6 
return 6

Evaluate
- Time Complexity: O(n) - going through each element in the list
- Space Complexity: O(1) - no data structs used
"""

def maxSubArray(nums):

    if not nums:
        return None

    maxSum = nums[0]
    curSum = 0

    for num in nums:

        # reset curSum if adding prev int made it neg
        if curSum < 0:
            curSum = 0

        curSum += num
        maxSum = max(curSum, maxSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]

print("Expected Output: ", 6)
print("Actual Output: ", maxSubArray(nums))

print("Expected Output: ", 23)
print("Actual Output: ", maxSubArray(nums2))
    
