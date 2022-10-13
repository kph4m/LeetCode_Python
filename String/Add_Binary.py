"""
Add Binary
Given two binary strings a and b, return their sum as a binary string.

Understand
- add two binary string and return their sum as a binary string
- 11 (3) + 1 (1) = 100 (4)

   11
    11
 +  11
   110

Match
- Binary Addition

Plan
- create carry variable
    - possible sums for addition
        - 1 + 1 + 1 = 3
        - 1 + 1 = 2
        - 1 + 0 = 1
    - to calculate the new carry, carry // 2
        - 3 // 2 = 1
        - 2 // 2 = 1
        - 1 // 2 = 0
- reverse a and b so we could loop easily
- iterate through max(a,b)
    - if i < len(a)
        - int(a)
    - else
        - 0
    - if i < len(b)
        - int(b)
    - else
        - 0
    - add both digits
    - convert to base 2
    - add to string
    - update carry
- if carry exists at the last calculation (1 not 0)
    - add 1 to the end string
- return string

Implement

Review
- 111 (7) + 11 (3)
- for i in range(3)
    - 1 + 1 + 0 = 2 % 2 = 0, res = 0, carry = 1
    - 1 + 1 + 1 = 3 % 2 = 1, res = 10, carry = 1
    - 1 + 0 + 1 = 2 % 2 = 0, res = 010, carry = 1
- extra carry, 1 + 111 = 1111

Evaluate
- Time Complexity: O(n), where n is the size of max(len(a),len(b))
- Space Complexity: O(n), reversing the strings
"""

def addBinary(a,b):

    # string we'll return
    res = ""

    # carry digit
    carry = 0

    # reverse the strings for easy loop
    a = a[::-1]
    b = b[::-1]

    # loop through all elements of biggest string
    for i in range(max(len(a), len(b))):
        # if doesn't exceed bounds, set normally
        if i < len(a):    
            intA = int(a[i])
        # exceeds bounds, set to 0
        else:
            intA = 0
        # if doesn't exceed bounds, set normally
        if i < len(b):
            intB = int(b[i])
        # exceeds bounds, set to 0
        else:
            intB = 0
        
        # get the total
        total = intA + intB + carry

        # convert to base 2
        totalB2 = str(total % 2)

        # add to result string
        res = totalB2 + res

        # update carry
        carry = total // 2
    
    # if carry exists at the end, add 1 to front of string
    if carry:
        res = "1" + res

    return res

print("Expected Output: 101")
print("Actual Output: ", addBinary("10", "11"))

print("Expected Output: 1010")
print("Actual Output: ", addBinary("111", "11"))