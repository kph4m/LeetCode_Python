"""
Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Understand
- given string expression, evaluate it and return the result of the evaluation
- will it always be valid?
    - yes
- what happens if there are no operators?
    - return none
- " 2-1 + 2 "
    - "2-1+2", [1]
        - "1+2" [3]
- 3-(1+2)

Match
- stack

Plan
- 3 different chars we can encounter
    - digits
    - operators (+, -)
    - parenthesis ()
- cur: keep track of current value (for parenthesis)
- res: final value
- sign: negative or positive
- stack: storing res and pos before going through parenthesis

Implement

Review
3-(1+2)

0 index
cur = 3

1 index
res = 3
sign = -1
cur = 0

2 index
[3,-1]
sign = 1
res = 0

3 index
cur = 1

4 index
res = 1
sign = 1
cur = 0

5 index
cur = 2

6 index
res = 3
res = -3 + 3 = 0

return 0

Evaluate
- Time Complexity: O(n) - go through entire string once
- Space Complexity: O(n) - stack could have n elements in the worse case ((((()))))

"""

def calculate(s):
    cur = 0
    res = 0
    sign = 1
    stack = []

    for char in s:
        if char.isdigit():
            cur = cur * 10 + int(char)
        elif char in ['+', '-']:
            # add previous char * sign to res
            res += sign*cur

            # reset sign to account for next digit value
            sign = 1 if char == "+" else -1

            # reset cur to setup for next value
            cur = 0

        elif char == "(":
            # keep track of res and sign when entering parenthesis
            stack.append(res)
            stack.append(sign)

            # reset sign and res
            sign = 1
            res = 0

        elif char == ")":
            # add last value to res 
            res += sign * cur

            # get sign and res from stack
            res *= stack.pop()
            res += stack.pop()

            # reset cur
            cur = 0
        
    # add any leftover values we didn't compute
    return res + sign * cur


print("Expected Output: 0")
print("Actual Output: ", calculate("3-(1+2)"))


print("Expected Output: 23")
print("Actual Output: ", calculate("(1+(4+5+2)-3)+(6+8)"))