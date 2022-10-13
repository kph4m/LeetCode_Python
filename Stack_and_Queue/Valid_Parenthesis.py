"""
Valid Parenthesis
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.

Understand
'(){}[][]' -> true
'({}[' -> false
'({)}' -> false 
'' -> false
'({})' -> true

Match
String traversal, checking correct string value using stack

Plan
create stack that will store the values
create dictionary to store closing parenthesis as keys and opening parenthesis as values
iterate through list
  check if it's a closing parenthesis
      check if the closing parenthesis has the corresponding opening parenthesis in the stack
          po it from the stack
  else, just append it to the stack
return True if the stack is empty, false otherwise

Implement

Review

s='{()}'
char = '{', stack = ['{']
char = '(', stack = ['{','(']
char = ')', matches stack pop, stack = ['{']
char = '}', matches stack pop, stack = []
stack empty, return True

s='{(})'
char = '{', stack = ['{']
char = '(', stack = ['{','(']
char = '}', doesn't match, return false

Evaluate
Time Complexity: O(n) - go through each char in the string once
Space Complexity: O(n) - stack could be up to the size of the input
"""

def isValid(s):

    # Stack to store non-closing parenthesis values
    # Space Complexity: O(n)
    stack = []
    closeList = { ')' : '(', '}': '{', ']' : '['} 

    # Iterate through string
    # Time Complexity: O(n)
    for char in s:
        # Closing parenthesis
        if char in closeList:
            # if stack exists and last element in stack is the corresponding opening of the current char
            if stack and stack[-1] == closeList[char]:
                # pop from stack
                stack.pop()
            else:
                return False

        # Opening parenthesis
        else:
            stack.append(char)

    # Only valid if the stack is empty (popped all parenthesis because they were valid)
    return True if not stack else False


s ='({})'
s2 = '})]'
s3 = ''
s4 = '(]'
s5 = '({})}'

if __name__ == "__main__":
    print("Expected Output: True")
    print("Actual Output:", isValid(s))

    print("Expected Output: False")
    print("Actual Output:", isValid(s5))


# Alt Solution without dictionary
def valid(s):

  if len(s) <= 1:
    return False
    
  stack = []

  # iterate through list
  for char in s:
    if (char == '(' or char == '[' or char == '{'):
      stack.append(char)
    else:
      if (char == ')'): 
        if (stack[-1] != '('): 
          return False
        else:
          stack.pop()
      if (char == ']'): 
        if (stack[-1] != '['): 
          return False
        else:
          stack.pop()
      if (char == '}'): 
        if (stack[-1] != '{'): 
          return False
        else:
          stack.pop()
  return True