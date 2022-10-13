"""
Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.


Understand
- given array where each character is a task
- each task done in one unit of time
    - each unit of time, could complete a task or just be idle
- n represents cooldown period between two same tasks
- return min unit of times to finish all tasks  

Match
- Max Heap to find the most frequent element


Plan
- do the most frequent task first
    - A,A,A,B,B,C,C, n =1
        - CBACBA_A = 8
        - CBCBA_A_A = 9
        - ABCABCA = 7 

- use maxheap to find most frequent elements
- use queue to store (task, what time we can insert the task back into the maxheap)

How to get most frequent elements?
    - Dictionary: Key = Task, Value = Frequency of task
    
Process the most frequent task
    - Sort it by value in decreasing order
    - MaxHeap
        - when we pop, we always get the max frequency task

Implement

Review
A,A,A,B,B,C,C, n = 1

maxHeap = [-3,-2,-2]

time = 1
maxHeap = [-2,-2]
queue = [[-2,2]]

time = 2
maxHeap = [-2,-2]
queue = [[-1,3]]

time = 3
maxHeap = [-2, -1]
queue = [[-1,4]]

time = 4
maxHeap = [-1,-1]
queue = [[-1,5]]

time = 5
maxHeap = [-1,-1]
queue = []

time = 6
maxHeap = [-1]
queue = []

time = 7
maxHeap = []
queue = []

queue and maxHeap empty, stop

return 7

Evaluate
- Time Complexity: O(n*len(tasks)), worse case each task is the same so need to take a break at each task
- Space Complexity: O(n) - dictionary, queue, O(1) - heapq
"""

import heapq
from collections import Counter, deque

def leastInterval(tasks, n):

    # create maxheap
    c = Counter(tasks)
    maxHeap = [-task for task in c.values()]
    heapq.heapify(maxHeap)

    # create queue
    queue = deque()

    # keep track of time
    time = 0

    while maxHeap or queue:
        time +=1

        # pop the value from maxheap
        # append (value+1, time until we can insert back into the heap)
        if maxHeap:
            value = 1 + heapq.heappop(maxHeap)
            # if its 0, don't add it back to the queue
            if value:
                queue.append([value, time+n])

        # insert value back into heap if time is good
        if queue and queue[0][1] == time:
            heapq.heappush(maxHeap, queue.popleft()[0])

    return time


print("Expected Output: 7")
print("Actual Output: ", leastInterval(["A","A","A","B","B","C","C"], 1))

print("Expected Output: 6")
print("Actual Output: ", leastInterval(["A","A","A","B","B","B"], 0))