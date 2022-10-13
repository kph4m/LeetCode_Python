"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Understand
- implement MinStack class (min element must be easy to access)
- push
    - [1,2,3]
    - push 4 -> [1,2,3,4]
    - pop -> 3
    - top -> 3
    - getMin -> 1
- what if stack doesn't exist?
    - pop - don't do anything
    - top - return none
    - getMin - return none

Match
- List for base stack
- Keep track of min value with every append
    - Tuple
    - additional stack for min values

Plan
Double Stack 
- init
    - list for base stack
    - list for min stack
- push
    - base.append(item)
    - get min value between recent value and current min value and append to min stack
- pop
    - pop from both base and min stack
- top
    - base[-1]
- getMin
    - min[-1]

Implement

Review
Double Stack
push -2
- base = [-2]
- min = [-2]

push 0
- base = [-2, 0]
- -2 < 0, -2 min
- min = [-2, -2]

push -3
- base = [-2,0,-3]
- -3 < -2, -3 min
- min = [-2,-2,-3]

pop
- base = [-2,0]
- min = [-2,-2]

top
- 0

getMin
- -2

Tuple
push -2
- [(-2,-2)]

push 0
- [(-2,-2), (0,-2)]

push -3
- [(-2,2), (0,-2), (-3,-3)]

pop
- [(-2,2), (0,-2)]

top
- 0

getMin
- -2

Evaluate

Double Stack
- init:
    - Time Complexity: O(1)
    - Space Complexity: O(n) - 2 list
- push
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- pop
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- top
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- getMin
    - Time Complexity: O(1)
    - Space Complexity: O(1)


Tuple
- init:
    - Time Complexity: O(1)
    - Space Complexity: O(n) - 1 list
- push
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- pop
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- top
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- getMin
    - Time Complexity: O(1)
    - Space Complexity: O(1)


"""

##### Double Stack Implementation #####

# class MinStack:

#     def __init__(self):
#         self.base = []
#         self.min = []
        

#     def push(self, val: int) -> None:
#         self.base.append(val)
#         # if min stack doesn't have any values yet, just use val
#         val = min(val, self.min[-1] if self.min else val)
#         self.min.append(val)
        
#     def pop(self) -> None:
#         self.base.pop() if self.base else None
#         self.min.pop() if self.min else None
        
#     def top(self) -> int:
#         return self.base[-1] if self.base else None
        
#     def getMin(self) -> int:
#         return self.min[-1] if self.min else None


#### Tuple Implementation #####

class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        # if min stack doesn't have any values yet, just use val
        minVal = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val,minVal))
        
    def pop(self) -> None:
        return self.stack.pop() if self.stack else None
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);

print("Expected Output: -3")
print("Actual Output: ", minStack.getMin())

minStack.pop();

print("Expected Output: 0")
print("Actual Output: ", minStack.top());    

print("Expected Output: -2")
print("Actual Output: ", minStack.getMin());    
