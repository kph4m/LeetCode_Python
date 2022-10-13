"""
Convert Int to Binary

Understand
- convert int input into binary
- 7
    - 8421
    -  111

7 // 2 = 3, 1
3 // 2 = 1, 1
1 // 2 = 0, 1

4 // 2 = 2, 0
2 // 2 = 1, 0
1 // 2 = 0, 1

Match
- Stack

Plan
- create stack to store modulo output in
- while n isn't 0
    - stack.append(n % 2)
    - n = n//2
- output=""
- while stack:
    - output+=stack.pop()
- return output

Implement

Review
4 // 2 = 2, stack = [0]
2 // 2 = 1, stack = [0]
1 // 2 = 0, stack = [1]
output = "100"

Evaluate
- Time Complexity: O(logn) - modulo while loop + O(n) - stack iteration = O(n)
- Space Complexity: O(n) - stack
"""


def convertToBinary(num):
    # Write your code here
    # return bin(num)[2:]

    if not num:
        return None

    stack = []
    
    while num != 0:
        stack.append(num % 2)
        num = num // 2
    
    output = ""
    
    while stack:
        output = output + str(stack.pop())
    
    return output

print("Expected Output: 111")
print("Actual Output ", convertToBinary(7))

print("Expected Output: 100")
print("Actual Output ", convertToBinary(4))

