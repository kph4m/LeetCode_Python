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
- Implement queue using only 2 stacks
    - queue = first in first out
    - stack = last in first out
- push = add element to queue
- top = check last element in queue
- pop 
    - queue: remove first element
    - stack: remove last element
- empty = check if no elements in queue

Match
- Stack, Queue  

Plan
- push should be the same, just push to last
- Top should be the same, just check the last element
- pop
    - [1,2,3], if we wanted to remove 3, we can easily using stack (remove right) but not queue (can only remove from left)
    - we want to remove all the elements except the last one, push them back to the queue, then we can remove the last element because it'll be the furthest left
        - [3,2,1]

Implement

Review
- [1,2,3]
- Push 4: [1,2,3,4]
- Pop 3: [1,2,3] -> [3,1,2] -> [1,2]
- Top: [3]
- Empty: len([1,2,3]) = 3 = False

Evaluate
    Deque Solution
        Time Complexity
            - Push: O(1)
            - Pop: O(n)
            - Top: O(1)
            - Empty: O(1)
        Space Complexity:
            - O(n)
    Queue Solution
        Time Complexity:
            - Push: O(n)
            - Pop: O(1)
            - Top: O(n)
            - 
"""
##### USING DEQUE #####
from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()    
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        # pop all prev elements and add it back to the end of the queue so the last element becomes the first element
        # [1,2,3,4] -> [4,1,2,3]
        for i in range(len(self.q) -1):
            self.q.append(self.q.popleft())
        print(self.q)
        # return first element
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        # return last element
        return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


##### USING QUEUE #####
# import queue
# class MyStack:
#     def __init__(self):
#         self.q = queue.Queue()

#     # f[1,2,3]r
#     # push(4) -> f[1,2,3,4]r -> f[4,3,2,1]r - can now pop from the front in the order that a stack wouldve gotten
#     def push(self, x: int) -> None:
#         self.q.put(x)
#         for i in range(self.q.qsize() - 1):
#             self.q.put(self.q.get())

#     # from our push method, we we arranged so front[1,2,3,4]rear of queue is now front[4,3,2,1], if we pop now, we get 4, which
#     # is what we wanted for stack [1,2,3,4]
#     def pop(self) -> int:
#         return self.q.get()

#     # f[1,2,3]r -> 1
#     # f[2,3,1]
#     # f[]
#     def top(self) -> int:
#         # get the top value
#         ret = self.q.get()
#         # push it back to the end of the queue
#         self.q.put(ret)
#         # bring it the front again
#         for i in range(self.q.qsize() - 1):
#             self.q.put(self.q.get())
#         return ret        

#     def empty(self) -> bool:
#         return self.q.qsize() == 0


myStack = MyStack();
myStack.push(1);
myStack.push(2);
myStack.push(3);
myStack.push(4);
print("Expected Output: 4"); 
print("Actual Output: ", myStack.top());

print("Expected Output: 4")
print("Actual Output: ", myStack.pop()); 

print("Expected Output: False")
print("Actual Output: ", myStack.empty()); 