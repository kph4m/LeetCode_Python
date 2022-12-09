"""
Find Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Understand
- find dupe number in array in constant space (can't use data structures)
- length of array = n+1
- each integer in the array is within 1 - n inclusive
    - each integer will be within a position in the array
- since there's a guaranteed dupe, there's a cycle if we move positions using integers
- [1,3,4,2,2]
    - 1 -> 3 -> 2 (beginning of cycle) -> 4 -> 2 -> 4

Match
- Floyd cycle detection

Plan
- find intersection point of slow (moves by 1) and fast (moves by 2) pointer to find dupe
    - this will past most testcases, but we'll need to do an additional iteration to pass all test cases
- reset slow, find intersection point of slow and fast again
    - fast will only move one at a time within the cycle

Implement

Review
- [1,3,4,2,2]

1 -> 3 -> 2 -> 4
slow = 1
fast = 1

slow = 3
fast = 2

slow = 2
fast = 2

2 is the intersection point

slow = 3
fast = 4

slow = 2
fast = 2

return 2

Evaluate

Unoptimal
- Time Complexity: O(n) - iterate dict
- Space Complexity: O(n) - dict

Optimal
- Time Complexity: O(n) - iterate array
- Space Complexity: O(1) - no data structures used
"""
from collections import Counter

def findDuplicate(nums):

    # Unoptimal solution using Counter
    # countNums = Counter(nums)

    # for key, value in countNums.items():
    #     if value == 2:
    #         return key
        
    # return (countNums.most_common()[0][0])


    # Optimal Solution using Cycle Detection
    # set slow and fast to beginning
    slow, fast = nums[0], nums[0]

    # find first intersection point
    while (True):
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break

    # reset slow
    slow = nums[0]

    # find second intersction point 
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow

print("Expected Output: 2")
print("Actual Output: ", findDuplicate([1,3,4,2,2]))

print("Expected Output: 3")
print("Actual Output: ", findDuplicate([3,1,3,4,2]))

print("Expected Output: 5")
print("Actual Output: ", findDuplicate([1,5,3,2,5,4]))