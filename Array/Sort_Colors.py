"""
Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Understand
- given array, sort them in-place so they're in the order 0,1,2
- [2,0,2,1,1,0] -> [0,0,1,1,2,2]
- leftmost must be smallest (0), rightmost must be largest (2)
- 3 pointers to indicate left boundary, current, and right boundary

Match
- Two Pointer, Partition

Plan
- iterate list
    - if current == 0
        - swap with left boundary
        - increment left pointer
        - increment cur pointer
    - if current == 2
        - swap with right boundary
        - decrement right poiner
        - don't change the cur pointer because it could swap to a value and get it stuck in the middle, need to check new i value
            - [0 1 2 1 0 2]
                 l i   r
            - [0 1 0 1 2 2]
                 l   i
                     r
            - 0 is now in the middle
    - if current == 1
        - increment the i pointer
        - we're already swapping to create the left and right bounds, don't need to mess with 1, it'll end up in the middle


Implement

Review
[2,0,2,1,1,0]
 l         r
 i 

swap r

[0,0,2,1,1,2]
 l       r
 i 

swap l

[0,0,2,1,1,2]
   l     r
   i 

swap l

[0,0,2,1,1,2]
     l   r
     i 

swap r

[0,0,1,1,2,2]
     l r
     i 

continue

[0,0,1,1,2,2]
     l r
       i 

stop


Evaluate
- Time Complexity: O(n) - going through all values once
- Space Complexity: O(1) - no data structures

"""
def sortColors(nums):

    l,r,cur = 0, len(nums) - 1, 0

    while cur <= r:
        if nums[cur] == 0:
            nums[cur], nums[l] = nums[l], nums[cur]
            l+=1
            cur+=1
        elif nums[cur] == 2:
            nums[cur], nums[r] = nums[r], nums[cur]
            r-=1
        else:
            cur+=1

    return nums


print("Expected Output: : [0,0,1,1,2,2]")
print("Actual Output: ", sortColors([2,0,2,1,1,0]))

print("Expected Output: : [0,1,2]")
print("Actual Output: ", sortColors([2,0,1]))