"""
Container with Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Understand
- given array with heights, return maximum amount of water a container can store
- the two ends cant be equal
- [1,3,6,3,7] -> 6-7 = 6*6 = 36
- if height doesn't exist or size of height is 1, return 0

Match
- Two pointer

Plan
- Two pointer
    - left = beginning, right = end
- create max variable
- while l < r
    - cal area
    - if cur area > old area, replace it
    - if height of left < height of right, increment left
    - if height of right < height of left, decrement right
    - if they're equal, increment/decrement left or right
- return max variable

Implement

Review
[1,4,3,7]
l = 0, r = 3, 3-0 = 3, area = 3 * 1 = 3
l = 1, r = 3, 3-1 = 2, area = 2 * 4 = 8
l = 2, r = 3, 3-2 = 1, area = 1 * 3 = 3

return 8

Evaluate
- Time Complexity: O(n) - go through each element in the array once
- Space Complexity: O(1) - no data structures used
"""

def maxArea(heights):

    if len(heights) <= 1:
        return 0
    
    l, r = 0, len(heights) - 1
    area = 0

    while l < r:
        curArea = (r-l) * min(heights[l], heights[r])

        area = max(area, curArea)

        if heights[l] < heights[r]:
            l += 1

        elif heights[r] < heights[l]:
            r -= 1

        else:
            r -= 1

    return area

print("Expected Output: 8")
print("Actual Output: ", maxArea([1,4,3,7]))

print("Expected Output: 49")
print("Actual Output: ", maxArea([1,8,6,2,5,4,8,3,7]))