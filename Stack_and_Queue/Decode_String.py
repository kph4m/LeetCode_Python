"""
Understand
- prior number indicates quantitiy of bracket
    - 2[a2[b]] -> 2[abb] -> abbabb
- need to go all the way, then work outwards
    - solve 2[b]
    - solve 2[abb]
- at what point do we start popping?
    - when we encounter a ']'
    - take all the values within the bracket, then copy them k number of times, where k is the number before the bracket

Match
- String Traversal, Maybe stack to backtrack?

Plan
- create stack
- iterate through string
    - if its not ], append to stack
    - if it is ]
        - create substring to add to the stack
        - while the top of the stack isn't [
            - substring = substring + stack.pop()
        - pop the [
        - create a variable to store the number
        - now to take of the number, it can be more than one digit
        - while top of the stack is a digit
            - k = stack.pop() + k
        - stack.append(k * substr)
- stack now contains all the elements, return string(stack contents)

Implement

Review
3[a2[c]]

stack = [3,'[',a,2,'[',c]

] detected, substring = c, pop c, stack = [3,'[',a,2,'[']
pop [
2 * c = cc
stack = [3,'[',a,cc]
] deteched, substring = acc, pop c,c,a, stack = [3, '[']
pop [
3 *acc = accaccacc
stack = ['accaccacc']

return 'accaccacc'

Evaluate
- Time Complexity: O(n) - iterate through encoded string
- Space Complexity: O(n) - stack
"""

def getDecodedString(encoded):
    # Write your code here
    
    stack = []
    
    for char in encoded:
        if char != ']':
            stack.append(char)
            
        # if its closing
        else:
            substring = ""
            # get all the chars in the bracket
            while stack[-1] != '[':
                substring = stack.pop() + substring
            
            # pop the [
            stack.pop()
            
            # get the number
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
                
            stack.append(int(k) * substring)
    
    # creates a string from the stack contents with nothing inbetween them
    return "".join(stack)


print("Expected Output: accaccacc")
print("Actual Output ", getDecodedString("3[a2[c]]"))

print("Expected Output: aaabcbc")
print("Actual Output ", getDecodedString("3[a]2[bc]"))

print("Expected Output: abcabccdcdcdef")
print("Actual Output ", getDecodedString("2[abc]3[cd]ef"))
                
        
