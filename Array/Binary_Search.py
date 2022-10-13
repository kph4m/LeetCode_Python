"""
Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Understand
- find the target in an array and return the index
- if target doesn't exist, return -1
- write in O(logn)

Match
- List

Plan
- create left and right pointer to partition subarray
- while the left pointer is less than or equal to right
- Find the middle element
- If its lower than the target, move to the right
- If its greater than the target, move to the left
- If it's equal, return m
- outside the while loop, return -1

Implement

Review
- nums = [1,2,3,4,5,6], target = 5
- l = 0, r = 5, m = 2, 5 > 3, move left pointer
- l = 3, r = 5, m = 4, nums[4] = 5, return m  

Evaluate
- Time Complexity: O(logn), we're halving the number of elements we check with each iteration 
- Space Complexity: O(1), we don't create any data structures

"""

def search(nums, target):
    
    # make sure values in nums and target is a number
    if len(nums) != 0:

        l, r = 0, len(nums)-1

        while l<=r:
            # calc middle element by floor(l+r / 2)
            m = (l + r) // 2
            # if current int less than target, move left pointer to m + 1
            if nums[m] < target:
                l = m + 1
            # if current int more than target, move right pointer to m - 1
            elif nums[m] > target:
                r = m - 1
            # if current int equals target, return m
            else:
                return m
    # if target not found, return -1
    return -1

nums = [1,2,3,4,5,6]

print("Expected Output", 4)
print("Actual Output",search(nums, 5))

print("Expected Output", -1)
print("Actual Output",search(nums, 7))



