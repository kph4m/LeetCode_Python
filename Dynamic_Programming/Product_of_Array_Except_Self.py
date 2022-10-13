"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Understand
- given list, return list where list[i] is product of all the other elements except for element at i
- [1,3,6,2] -> [36, 12, 6, 18]
- elements can be negative
- what if there's only 1 value?
    - return 0

Match
- Prefix / Postfix

Plan
- create res array
- calculate the Prefix and Postfix
- multiply the values that sandwich i 
    - [1,2,3,4]
    - Prefix:   [1,2,6,24]
    - Postfix: [24,24,12,4]
    - Output:
        - 0: 1 * 24 = 24
        - 1: 1 * 12 = 12
        - 2: 2 * 4 = 8
        - 3: 6 * 1 = 6
        - [24,12,8,6]
        
Implement

Review
[1,2,3,4]

prefix = 1

i=0
res = [1]
prefix = 1

i=1
res = [1,1]
prefix = 2

i=2
res = [1,1,2]
prefix = 6

i=3
res = [1,1,2,6]
prefix = 24

[1,1,2,6]

postfix = 1

i=3
res = [6]
postfix = 4

i = 2
res = [8,6]
postfix = 12

i = 1
res = [12,8,6]
postfix = 24

i = 0
res = [24,12,8,6]
postfix = 24

return [24,12,8,6]


Evaluate
- Time Complexity: O(n) - iterate list 2 times (prefix and postfix)
- Space Complexity: O(n) - list with n elements
"""

def productExceptSelf(nums):

    res = [1] * (len(nums))

    # prefix
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    print(res)

    # postfix
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        print(postfix)
    return res

print("Expected Output: [24,12,8,6]")
print("Actual Output: ", productExceptSelf([1,2,3,4]))

print("Expected Output: [0,0,9,0,0]")
print("Actual Output: ", productExceptSelf([-1,1,0,-3,3]))


