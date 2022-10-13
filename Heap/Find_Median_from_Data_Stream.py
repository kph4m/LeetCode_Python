"""
Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Understand
- MedianFinder
    - stores the numbers in order
- addNum
    - adds the number to the list, maintaining the order
- findMedian
    - returns median of numbers in the list
    - even: return mean of 2 center numbers
    - odd: return center number
- ex
    - add 5, [5]
    - add 1, [1,5]
    - add 2, [1,2,5]
    - findMedian(), 2
    - add 3, [1,2,3,5]
    - findMedian(), 2+3 / 2 = 2.5

Match
- Heap

Plan
- create two heaps: one for the lower half, one for the upper half
    - lower half will be a max heap, top will be easily accessible
    - upper half is a min heap, bottom will be easily acessible
    - this allows us to easily access the center values 
- conditions to account for
    - make sure they're as equal as possible (both n/2 or one of them is n/2 + 1)
    - make sure the lower half only has values that are less than the upper half
- when finding median
    - odd and even conditions

- MedianFinder()
    - create array for small and large halves
- addNum
    - append to small
    - check if its in the right position
        - if not, pop and push it to large
    - check if each halves are relatively equal size
        - if not, adjust greater half by popping and adding to lower half
- findMedian
    - if its even, get the two values at the top of each heap and divide by 2
    - if its odd, the center will be the top of the greater half

Implement

Review
small = [], large = []

- add 5, small = [-5]
- add 1, small = [-1,-5], small = [-1], large = [5]
- add 2, small = [-1,-2], large = [5]
- findMedian(), small[0] = -2
- add 3, small = [-1,-2,-3], small = [-1,-2], large = [3,5]
- findMedian(), small[0] + large[0] / 2 = 2 + 3 /2 = 2.5

Evaluate
- Time Complexity: O(logn) - heap operations, O(1) - findMedian
- Space Complexity: O(n) - two heaps whose elements summed are equal to number of elements
"""
from collections import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 *num )

        # check if all values in small are smaller than all large values
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        # check if one of them is too big (2+ more elements)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)


    def findMedian(self) -> float:
        # odd length
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        # even lengths
        if len(self.small) == len(self.large):
            return (((-1 * self.small[0]) + self.large[0]) / 2)
