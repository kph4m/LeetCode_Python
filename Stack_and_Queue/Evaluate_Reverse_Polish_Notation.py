"""
Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


Understand
- Postfix expression
    - use operator to compute the 2 previous operands
- ["2","1","+","3","*"] -> 9
    - ((2 + 1) * 3) = 9

Match
- Stack

Plan
- create stack
- loop through list
    - if its a number, push it to the stack
    - if its an operand, 
        - pop 2 values from stack and perform the operation using the operand
        - append result in stack
- return stack.pop()

Implement

Review
["2","1","+","3","*"] -> 9
- stack = []
- stack = [2,1]
- encounter +, pop 1 and 2 from the stack
    - res = 1 + 2
    - append 3 to stack
- stack = [3]
- stack = [3,3]
- encounter *, pop 3 and 3 from teh stack
    - res = 3 * 3
    - res = 9
    - append 9 to stack
- return 9

Evaluate
- Time Complexity: O(n) - go through each element once
- Space Complexity: O(n) - stack could have same number of elements as the input
"""

def evalRPN(tokens):

    stack = []

    for token in tokens:
        # if its a number, push to stack
        if token not in "+-*/":
            stack.append(int(token))

        # if its an operator
        else: 
            # store result of operation
            res = 0

            # get both values to operate on
            value2 = stack.pop()
            value1 = stack.pop()

            if token == "+":
                res = value1 + value2
            elif token == "-":
                res = value1 - value2
            elif token == "*":
                res = value1 * value2
            else:
                res =  int(value1 / value2)

            stack.append(res)
    
    # end result should be the only one remaining in the stack
    return stack.pop()
    
print("Expected Output: 9")
print("Actual Output: ", evalRPN(["2","1","+","3","*"]))

print("Expected Output: 6")
print("Actual Output: ", evalRPN(["4","13","5","/","+"]))

print("Expected Output: 22")
print("Actual Output: ", evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

