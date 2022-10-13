"""
Shortest Unsorted Continuous Subnumsay

Given an integer numsay nums, you need to find one continuous subnumsay that if you only sort this subnumsay in ascending order, then the whole numsay will be sorted in ascending order.

Return the shortest such subnumsay and output its length.'

Understand
- given numsay of ints, find the shortest continuous subnumsay that when sorted, will sort the entire numsay. Return the length of it
- nums = [2,6,4,8,10,9,15]
    - subnumsay to sort = [6,4,8,10,9]
    - return 5
- nums = [1,2,3,4]
    - already sorted
    - return 0

Match
- Lists

Plan
- create left (beginning) and right (end) pointer
- iterate left to right
    - at the first instance where curr.next < curr, set left pointer to curr
- iterate right to left
    - at the first instance where curr.next > curr, set right pointer to curr
- if right == left, the array is already sorted
    - return 0
- find the min and max in the subarray
- loop through the left and right side of the subarray, if they're in between min and max, expand the subarray to include them
- return right - left + 1

Implement

Review
[1, 3, 2, 0, -1, 7, 10]
- 3 is the first instance of unorder going from left to right, mark left as 1
- -1 is the first instance of unorder going from right to left, mark right as 4
- subarray = [3,2,0,-1]
- min = -1, max = 3
- go through all numbers outside subarray, if its within -1 - 7, include them in subarray
    - 1 is between -1 and 7, left = 0
    - 7 isn't between -1 and 3, exclude
- new subarray = [1,3,2,0,-1]
- return 5


Evaluate
- Time Complexity: O(n) - separate while loops
- Space Complexity: O(1) - don't create any other data structures

"""

# def findUnsortedSubnumsay(nums):

#     start = 0
#     end = 0

#     min = nums[len(nums) -1]
#     max = nums[0]

#     for i, num in enumerate(nums):
#         max = max(nums, max)
#         if nums[i] > max:
#             end = i

#     for i, num in enumerate(range(len(nums)-1, 0,-1)):
#         min = min(nums, min)
#         if nums[i] > min:
#             start = i

#     return end - start + 1


def findUnsortedSubarray(nums):
    if len(nums) < 2:
        return 0 

    # Initializing left and right pointers
    left, right = 0, len(nums) - 1

    # Incrementing left and right pointers
    while left < right:
        if nums[left] <= nums[left + 1]:
            left += 1
        else:
            break

    while right > left:
        if nums[right] >= nums[right - 1]:
            right -= 1
        else:
            break

    # Array is already sorted
    if left == right: 
        return 0

    # Find the max of the subnumsay

    saMax = max(nums[left:right+1])
    saMin = min(nums[left:right+1])

    # Adusting the subarray 

    while (left > 0 and nums[left - 1] > saMin): 
        left -= 1

    while (right < len(nums) - 1 and nums[right + 1] < saMax):
        right += 1

    return right - left + 1