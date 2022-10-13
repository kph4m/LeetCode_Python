"""
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Understand
- given array with heights, return the rectangle with the largest array

Match
- Stack

Plan

Brute Force
- calculate each possible area and store the max
- Time Complexity: O(n^2)

Optimized
- Create stack in ascending order

Implement

Review
[2,1,5,6]
[2,1,5,6,0]

stack = [0]

STACK = []
H = 2
W = 1
MX = 2
stack = [1]

stack = [1,2]

stack = [1,2,3]
stack = [1,2]
H = 6
W = 4 -2 - 1 = 1
mx = 6

stack = [1]
H = 5
W = 4-1-1 = 2
mx = 10

stack = []
H = 1
W = 4
hw = 4

stack = [4]

return 10

Evaluate

Brute Force
- Time Complexity: O(n^2), double for loop
- Space Complexity: O(1), no data structure used

Optimized
- Time Complexity: O(n), visit each height once
- Space Complexity: O(n), worse case stack contains n elmeents (1,2,3,4,5)
"""
def largestRectangleArea(heights):

    # Brute Force
    n = len(heights)
    mx = 0

    for i in range(n):
        for j in range(i, n):
            # get height
            h = min(heights[i:j+1])

            # get width
            w = j-i+1

            print(w,h)

            # set mx
            mx = max(mx, h*w)

    return mx

    # Optimized Solution

    # stack, mx = [], 0

    # # loop through heights
    # # add zero to heights so 0 is the absolute min and we don't calculate every single area
    # for i, h in enumerate(heights+[0]):
    #     # while stack exists and current height less than one on the stack (if it stops ascending)
    #     while stack and h < heights[stack[-1]]:
    #         H = heights[stack.pop()]
    #         if not stack:
    #             W = i
    #         else:
    #             W = i - stack[-1]-1
    #         mx = max(mx, W * H)
        
    #     # add to stack if its ascending
    #     stack.append(i)

    # return mx

print("Expected Output: 10")
print("Actual Output: ", largestRectangleArea([2,1,5,6]))

print("Expected Output: 4")
print("Actual Output: ", largestRectangleArea([2,4]))