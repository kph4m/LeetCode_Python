"""
Implement Queue from Stack
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Understand
- queue = first in, first out
- stack = last in, first out


Match
- Stack
- Queue

Plan
    Create two lists that will serve as the stacks

    Push(4)
    - s1 = [(back) 3,2,1 (front)], pop all element and store them in s2
    - s2 = [1,2,3], push the element into s1, s1 = [4]
    - put the s2 elements back into s1, s1 = [ (back) 4,3,2,1 (front)]

    Pop
    - pop s1

    Peek
    - look at the last element in s1

    Empty
    - check length of s1 if its empty

Implement

Review
[(back) 3,2,1 (front)]
Push
- s1 = [], s2 = [1,2,3] 
- s1 = [4]
- s1 = [4,3,2,1]
Pop: 1
Peek: 1
Empty: False

Evaluate
    Time Complexity
        Push: O(n)
        Pop: O(1)
        Peek: O(1)
        Empty: O(1)
"""

class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # pop all the elements in s1 into s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # append the element to s1
        self.s1.append(x)

        # pop all the elements in s2 back into s1
        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0


