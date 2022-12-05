"""
Maximum Product Subarray

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Understand
- find subarray with the max product

- Input: [-5,2,-3,-2]
- Output: 30 ([-5,2,-3])

- Input: [-5,-3,-2]
- Output: 30 ([-5,2,-3])


- Can they all be negative?
    - Yes

Match
- sliding window

Plan

Naive
- go through each subarray, calc the product, find max one

Attempt at Optimal
- pointers on each side
- if the product of all the elements in the subarray are negative
    - cut the negative value if it exists
        - if there's two negative values, cut the greatest negative
    - if they're both positive
        - cut the greatest positive number
-  if the product of all the elements in the subarry are positive
    - we found the max subarray, cutting anymore will just reduce it
    - return the product


Optimal
- find the max and minimum of each subarray

Implement

Review

[2,3,-2,4]

curMax: 2
curMin: 2
Res: 2

curMax: 6
curMin: 3
Res: 6

curMax: -2
curMin: -12
Res: 6

curMax: 4
curMin: -48
Res: 6

Return 6

Evaluate

Naive
- Time Complexity: O(n^2)
- Space Complexity: O(1)

Optimal
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

def maxProduct(nums):

    # Naive
    # result = nums[0]
    # for i in range(len(nums)):
    #     curResult = nums[i]
    #     for j in range(i+1, len(nums)):
    #         result = max(curResult, result)
    #         curResult *= nums[j]
    #     result = max(result, curResult)    
    # return result

    # Attempt at Optimal: 

    # if len(nums) == 1:
    #     return nums[0]

    # # Set pointers
    # l = 0
    # r = len(nums)


    # while l != r-1:

    #     curProd = 1

    #     # calc the product of the subarray
    #     for num in nums[l:r]:
    #         curProd *= num

    #     # if negative
    #     if curProd <= 0:

    #         # if they're both neg
    #         if nums[l] < 0 and nums[r-1] < 0:
    #             if abs(nums[l]) > abs(nums[r-1]):
    #                 r -= 1
    #             if abs(nums[r-1]) > abs(nums[l]):
    #                 l += 1

    #         # if they're both pos
    #         elif nums[l] >= 0 and nums[r-1] >= 0:
    #             if nums[l] == 0 or nums[r-1] == 0:
    #                 if nums[l] == 0:
    #                     l+=1
    #                 elif nums[r] == 0:
    #                     r-=1
    #             else:
    #                 if nums[l] > nums[r-1]:
    #                     l += 1
    #                 if nums[r-1] > nums[l]:
    #                     r -= 1

    #         # if one neg
    #         elif nums[l] < 0 and nums[r-1] >= 0:
    #             l += 1

    #         elif nums[r-1] < 0 and nums[l] >= 0:
    #             r -= 1

    #     elif curProd > 0:
    #         return curProd

    # return nums[l]

    # Optimal

    res = nums[0]

    curMin, curMax = 1,1

    for num in nums:
        tmp= curMax * num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, num * curMin, num)
        res = max(res, curMax)
    return res

print("Expected Output: 6")
print("Actual Output: ", maxProduct([2,3,-2,4]))

print("Expected Output: 0")
print("Actual Output: ", maxProduct([-2,0,-1]))

print("Expected Output: 2")
print("Actual Output: ", maxProduct([0,2]))

print("Expected Output: 30")
print("Actual Output: ", maxProduct([-5,2,-3,-2]))

print("Expected Output: 8")
print("Actual Output: ", maxProduct([-4,0,2,4]))