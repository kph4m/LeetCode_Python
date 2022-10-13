"""
K Largest Element Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.


Understand
- find k larget element array
- [1,4,2,5,3], k = 5 -> 5
- what if k > len(arr)?
    - return None


Match
- Sorting
- Heap
- Quick Select
    - Average Time Compelxity (equal halves): O(n)
    - Worse Time Complexity (non-equal halves): O(n^2)
    - Choose pivot (usually last)
    - First half of array: <= pivot
    - Second half of array: > pivot
    - Have pointer that goes from left to right
        - assign the correct values at the pointer
        - once you assign a value, increment the pointer

Plan

Built-in Sorting Solution:
- Sort array reverselt using built-in function
- return k-1 element

Min Heap Solution
- heapify the array so it's a min heap
- length = len(arr)
- while length > k: (this will go through until the k value is the root)
    - pop
    - len(arr) - 1
- return heap[0]

Quick Select
- 


Implement

Review
[3,2,1,5,6,4], k = 2

Built-in sorting solution
- Sort: [6,5,4,3,2,1]
- return k-1 = 5

Heap
- Heapify: [1,2,3,6,5,4] (not guaranteed to be sorted)
- length = 6
- while 6 > 2:
    - pop 1
    - length = 5
- while 5 > 2:
    - pop 2
    - length = 4
- while 4 > 2:
    - pop 3
    - length = 3
- while 3 > 2:
    - pop 4
- while 2 > 2: exit loop
- final heap: [5,6]
- return heap[0] = 5

Quick Select
[3,2,1,5,6,4], k = 2
- k = 6-2 = 4
- pivot = 4, p = 0
- 3 <= 4, [3], p = 1
- 2 <= 4, [3,2], p = 2
- 1 <= 3, [3,2,1], p = 3
- 5 !<= 4, p =3
- 6 !<= 4, p = 3
- swap 4 pivot and 4 point, [3,2,1,4,6,5]
- 3 < 4, focus on right half [5,6]
- pivot = 5 , p = 4
- swap 6 pivot and 5 point, [3,2,1,4,5,6] 
- 4 p = 4 k, return nums[4] = 5  

Evaluate

Built-in Sorting Solution:
- Time Complexity: O(nlogn)
- Space Complexity: O(n)

Heap
- Time Complexity: O(nlogn)
- Space Complexity: O(n)

Quick Select:
- Time Complexity: O(n) - recurses only on one side 
- Space Complexity: O(n) - recursive call stack

"""

import heapq

def findKthLargest(nums, k):

    # Built-in Sort Implementation
    # nums.sort(reverse=True)
    # return nums[k-1]

    # Min Heap Implementation
    # heapq.heapify(nums)

    # length = len(nums)

    # while length > k:
    #     heapq.heappop(nums)
    #     length -= 1
    
    # return nums[0]

    # Quick Select

    # Since we're sorting in ascending order, this makes it easier to find the kth largest value
    k = len(nums) - k

    def quickSelect(l,r):
        # Num we're gonna compare with all the values
        pivot = nums[r]

        # Pointer for left half values
        p = l

        # Iterate everything excluding the last element
        for i in range(l, r):
            # If less, assign to left half of array
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
            
        # After iterating through, assign pivot to pointer
        nums[p], nums[r] = nums[r], nums[p]

        # If p less than k, check the left half
        if p > k: 
            return quickSelect(l, p-1)
        # If p greater than k, check the right half
        elif p < k:
            return quickSelect(p+1, r)
        # If its equal, we found the kth greatest element, return nums[p]
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1 )

print("Expected Output: 5")
print("Actual Output: ", findKthLargest([3,2,1,5,6,4], 2))

print("Expected Output: 4")
print("Actual Output: ", findKthLargest([3,2,3,1,2,4,5,5,6], 4))

            


