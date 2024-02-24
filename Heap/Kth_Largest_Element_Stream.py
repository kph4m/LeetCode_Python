"""
Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Understand
- k represents the kth largest element to return from a stream
- add will append the integer to the nums, and will return the kth largest element

Match
- Heap

Plan
- init
    - init heap using heapify
    - pop smallest element if heap is larger than k to ensure first element in the heap is the kth largest
- add
    - if length of the heap less than k, just add the val
    - if val is greater than the first element, replace the first element with the val
    - if val is less than the first element, don't do anything
    - return the first element in the heap, which represents the kth largest element in the heap

Implement

Review

Evaluate
- Time Complexity: O(n) for heapification, O(n-k * log(n-k)) for while loop because the loops runs until the length of the heap is reduced to k (n-k) and heappop is log(number of elements its get called on) which is n-k
- Space Complexity: O(k), store k items in the heap
"""
import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)    
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # add to heap if heap is less than k, this will automatically rearrange the heap so that the smallest element is first
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # if the val is larger than the smallest element, replace the smallest element with the val so val is now the smallest element in the heap
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
    
# Testing
kthLargest = KthLargest(3, [4,5,8,2])
print(kthLargest.heap)
print("Add 3", "Should Return 4", kthLargest.add(3), kthLargest.heap)  
print("Add 5", "Should Return 5", kthLargest.add(5), kthLargest.heap)  
print("Add 10", "Should Return 5", kthLargest.add(10), kthLargest.heap) 
print("Add 9", "Should Return 8", kthLargest.add(9), kthLargest.heap)  
print("Add 4", "Should return 8", kthLargest.add(4), kthLargest.heap) 