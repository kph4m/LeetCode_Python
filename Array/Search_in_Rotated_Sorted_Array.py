"""
Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Understand
- given array of nums in asending order and rotated at an unknown pivot index, return the index of the target int if in nums, -1 if not in nums
- what if there's only 1 value?
    - return it

Match
- modified binary search

Plan
- create initial left and right pointer
    - while left < right
        - compute middle value
        - if target = middle, return middle
        - if left or right or middle equal to target, return index
        - if target is between L and M, search in the left side
        - if target is between M ad R, search in the right side
- return -1


Implement

Review
[4,5,6,0,1,2,3], targ = 2
l = 0, mid = 3, r = 6

l = 4, mid = 5, right = 6
nums[5] = 2 = targ

return 5

Evaluate
- Time Complexity: O(logn)
- Space Complexity: O(1)
"""

def search(nums, target):
    if not nums:
        return None

    if len(nums) == 1:
        if nums[0] == target:
            return 0
    
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # check right side condition

        
        
        if nums[left] <= nums[mid]:
            # [4,5,6,7,0,1,2], targ = 0
            if target < nums[left]:
                left = mid + 1
            # [2,3,4], targ = 4
            elif target > nums[mid]:
                left = mid + 1
            # check left
            # [2,4,5,7,1]
            else:
                right = mid - 1

        # check left side condition
        else:
            # [5,1,2,3,4], target 5
            if target > nums[right]:
                right = mid - 1
            # [1,2,3,4,5], target =2
            elif target < nums[mid]:
                right = mid - 1
            # check right
            # [4,5,6,0,1,2,3]
            else:
                left = mid + 1
    return -1


print("Expected Output: 5")
print("Actual Output ", search([4,5,6,0,1,2,3], 2))

print("Expected Output: -1")
print("Actual Output ", search([4,5,6,7,0,1,2], 3))

