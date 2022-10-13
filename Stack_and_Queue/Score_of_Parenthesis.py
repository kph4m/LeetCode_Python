"""
Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Understand
- given balanced string, return score
- score based on closed parenthesis
    - "(())" = 2
    - "()()" = 2
    - "(()(()))" = 6 
- nested: 2 * inner parenthesis
    - (()) = 1 * 2
- adjacent: add them
    - ()() + 2
- what if its empty
    - return 0
- always gonna be balanced

Match
- Stack

Plan
- create stack
- create score variable
- iterate through string
    - if its an opening parenthesis, append to stack
    - if its closing
        - pop from stack
        - if its opening append 1 since () = 1
        - if its closing
            - sum all number in the stack until top element is '('
            - multiply 2 to sum since nested parenthesis are multipled by 2
- return sum(stack)

Implement

Review
(()(()))

stack = ["("]
stack = ["(", "(",]

), pop (, stack = ["(", 1]

stack = ["(", 1, "(", "("]

), pop (, stack = ["(", 1, "(", 1]

), pop 1, stack = ["(", 1, "(",], tmp = 1, pop (, stack = ["(", 1], 2 * 1 = 2, stack = ["(", 1, 2]

), pop 2, stack = ["(", 1], tmp = 2, pop 1, stack = ["("], temp = 2 + 1 = 3, pop "(", stack = [], 2 * 3 = 6, stack = [6]

return 6


Evaluate
- Time Complexity: O(n) - iterate string + O(n/2) - iterate stack = O(n)
- Space Complexity: O(n) - stack
"""

def scoreOfParenthesis(S):

    # store parenthesis and values
    stack = []

    # iterate through parentheses
    for p in S:

        # if its an opening parenthesis, append normally to stack
        if p == "(":
            stack.append(p)

        # if its not an opening parenthesis, start popping and keeping track of score
        else:
            popped = stack.pop()

            # if its just one complete parenthesis, append value 1
            if popped == "(":
                stack.append(1)
            
            else:
                # if its not (, it can only be a number
                tmp = 0

                # add the # values in the stack to temp as long as its not closing
                while popped != "(":
                    tmp += popped
                    popped = stack.pop()
                
                # once all the values and the closing ( is removed, nested parenthesis is done so multiply by 2
                stack.append(2 * tmp)
    
    # after it iterates through the entire string, the final value should be the sum of the stack, return it    
    return sum(stack)


print("Expected Output: 2")
print("Actual Output: ", scoreOfParenthesis("()()"))

print("Expected Output: 2")
print("Actual Output: ", scoreOfParenthesis("(())"))

print("Expected Output: 6")
print("Actual Output: ", scoreOfParenthesis("(()(()))"))
