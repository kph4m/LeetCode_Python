"""

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Understand
- Given a size, return the sum average of a k-size window of ints
- 

Match
- Queue

Plan
- init
  - use deque
  - size
- next
  - if size or next value is none
    - return 0
  - if length of queue is the same as the input size
    - pop left, append the value
  - else
    - append the value
  - return sum of the ints in the queue / length of the queue

Evaluate
Time Complexity
- next: O(n)
Space Complexity
- init: O(n)
"""

from collections import deque 

class MovingAverage:
  
    def __init__(self, size: int):
      # init deque
      self.queue = deque()
      self.size = size
        
    def next(self, val: int) -> float:
      # edge cases
      if self.size is None or val is None:
        return 0

      # if len of queue equal size of moving window, pop first val, append new val
      if len(self.queue) == self.size:
        self.queue.popleft()
        self.queue.append(val)
      # if less than, just append
      else:
        self.queue.append(val)
      # return avg
      return sum(self.queue) / len(self.queue)


movingAverage = MovingAverage(3);
print(movingAverage.next(1)) # return 1.0 = 1 / 1
print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3


