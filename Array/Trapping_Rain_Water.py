"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Understand
- array representing elevation map, compute how much rain water it can hold

Match
- Two Pointer

Plan
- left, right converging to middle
- maxl, maxr to keep track of max walls on either side 
that we can use to subtract to get the area
- area: add area from both sides by doing maxl or maxr - current l height or r height
- if left < right, want to increment the left
- if right < left, want to increment the right
    - this helps account for not counting the biggest height when calculating water area, want to use the min height between two walls instead of the largest one

Implement

Review
[0,1,0,3,2,5]

maxl = 3
maxr
area = 2

return 2

Evaluate
- Time Complexity: O(n), go through each input once
- Space Complexity: O(1), didn't use any data structures
"""

def trap(height):

    if not height:
        return 0

    area = 0
    l, r = 0, len(height) - 1
    maxl, maxr = 0,0

    while l < r:
        if height[l] < height[r]:
            if maxl < height[l]:
                maxl = height[l]
            else:
                area += maxl - height[l]
            l+=1
        # if r < l or r == l
        else:
            if maxr < height[r]:
                maxr = height[r]
            else:
                area += maxr - height[r]
            r-=1
    return area

print("Expected Output: 2")
print("Actual Output: ", trap([0,1,0,3,2,5]))

print("Expected Output: 6")
print("Actual Output: ", trap([0,1,0,2,1,0,1,3,2,1,2,1]))