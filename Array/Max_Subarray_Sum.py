"""
Understand
- given positive int array and k, find max sum subarray with a size of k and return the sum
- [1,3,4,5,2], k = 3
    - max sum subarray with size of 3 = [3,4,5]
- [1,23,4,3], k = 5
    - return -1, len(arry) < k

Match
- Two Pointer

Plan
- check if len(array) >= k
- create max variable
- create left and right pointer to traverse array with size k
- iterate through array while right exists
    - if current subarray sum greater than max, replace with max
    - left + 1, right + 1
- return max

Implement

Review
[1,23,4,3], k=3
- left = 0, right = 3
    - left: right = [1,23,4] = 28 > 0, max = 28
- left = 1, right = 4
    - left:right = [23,4,3] = 30 > 28, max = 30
- left = 2, right = 5, right out of bounds, exit while loop
- return 40

Evaluate
- Time Complexity: O(n*k) - iterate through array and get the sum of k elements
- Space Complexity: O(1) - no data structures created

"""

def getMaxSum(arr, k):
    # Write your code here
    
    if k > len(arr):
        return -1
    
    max = 0
    
    left, right = 0, k
    
    while right <= len(arr):
        curSum = sum(arr[left:right])
        print(curSum)
        if curSum > max:
            max = curSum
        left+=1
        right+=1

    return max