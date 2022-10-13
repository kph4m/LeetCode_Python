"""
Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
         
Understand
- nums1 size of nums1 + nums2
    - followed by size(nums2) 0s
- make changes to nums1 in place, don't return anything
- if nums1 or nums2 doesn't exist, return none
Match
- Two Pointer, Runner Pointer to keep track of current value

Plan
Using two pointer technique, let small point to arr_small[arr_small.length - 1] and big point to arr_big[arr_big.length - 1]. Use another pointer, runner, to point to the last index in arr_big. Then, while the pointers are in range: {If arr_big[big] > arr_small[small], then assign arr_big[runner] = arr_big[big], and decrement big and runner. Otherwise, assign arr_big[runner] = arr_small[small], then decrement small and runner. }

Implement

Review
[1, 3, 7, 8, 15, 25, 0, 0, 0, 0], [-1, 4, 10, 11]
                 big          run             small
                 
[1, 3, 7, 8, 15, 25, 0, 0, 0, 25], [-1, 4, 10, 11]
             big           run                small
             
             
[1, 3, 7, 8, 15, 25, 0, 0, 15, 25], [-1, 4, 10, 11]
         big           run                    small

[1, 3, 7, 8, 15, 25, 0, 11, 15, 25], [-1, 4, 10, 11]
         big        run                    small

[1, 3, 7, 8, 15, 25, 10, 11, 15, 25], [-1, 4, 10, 11]
         big     run                     small

[1, 3, 7, 8, 15, 8, 10, 11, 15, 25], [-1, 4, 10, 11]
      big    run                         small

[1, 3, 7, 8, 7, 8, 10, 11, 15, 25], [-1, 4, 10, 11]
   big   run                            small

[1, 3, 7, 4, 7, 8, 10, 11, 15, 25], [-1, 4, 10, 11]
   bigrun                           small

[1, 3, 3, 4, 7, 8, 10, 11, 15, 25], [-1, 4, 10, 11]
bigrun                              small

[1, 1, 3, 4, 7, 8, 10, 11, 15, 25], [-1, 4, 10, 11]
run                                 small

[-1, 1, 3, 4, 7, 8, 10, 11, 15, 25], [-1, 4, 10, 11]


Would big ever exist when small is gone?

[1, 3, 7, 8, 15, 25, 0, 0, 0, 0], [26,27,28,29,30]
                 big          run             small

[1, 3, 7, 8, 15, 25, 0, 0, 0, 0], [-3, -2, -1, 0]
                 big          run             small


Evaluate
- Time Complexity: O(m + n) - iterate through all els in both lists once
- Space Complexity: O(1) - no data structures used



"""

def mergeArrays(nums1, nums2):

    # Write your code here
    n = len(nums2)
    m = len(nums1) - n

    runner, big, small = m + n -1, m-1, n-1
    
    while big >=0 and small >=0:
        if nums1[big] > nums2[small]:
            nums1[runner] = nums1[big]
            big -= 1
            runner -= 1
        else:
            nums1[runner] = nums2[small]
            small-=1
            runner -= 1
    
    # case where big is depleted by small has smaller values
    while small >= 0:
        nums1[runner] = nums2[small]
        small-=1
        runner -= 1
    
    return nums1


print("Expected Output: [-1, 1, 3, 4, 7, 8, 10, 11, 15, 25]")
print("Actual Output: ", mergeArrays([1, 3, 7, 8, 15, 25, 0, 0, 0, 0],[-1, 4, 10, 11]))

print("Expected Output: [1]")
print("Actual Output: ", mergeArrays([1], []))


print("Expected Output: [1,2,2,3,5,6]")
print("Actual Output: ", mergeArrays([1,2,3,0,0,0], [2,5,6]))