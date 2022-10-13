"""
Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Understand
- given array of ints nums, find the next permutation 
- next permutation based on lexicographic
    - if not possible, array arranged as lowest possible order (sorted in ascending order)
- [1,2,3] -> [1,3,2]
- [1,3,2] -> [2,1,3]
- [1] -> [1]
- empty?
    - return None
- any duplicates?
    - yes

Match
- 

Plan
- Find pivot point where, starting from the right, it stops increasing
    - [1 3 5 4 3 2 1] -> [5 4 3 2 1]
    - pivot point = 3
- Find lowest number in that sequence that goes after pivot point (not equal) and swap them
    - 4
    - [1 3 5 4 3 2 1] -> [1 4 5 3 3 2 1]
- Sort the sequence by ascending order (ie reverse)
    - [1 4 5 3 3 2 1] -> [1 4 1 2 3 3 5]

Implement

Review
[1 3 5 4 3 2 1]

pivot = 3
swap with 4

[1 4 5 3 3 2 1]

reverse sequence
[1 4 1 2 3 3 5]

Evaluate
- Time Complexity: O(n), worse case we'll go through the entire string for the sequence (3,2,1)
- Space Complexity: O(1), modify the input string only
"""

def nextPerm(nums):

    def reverse(nums,l,r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


    if len(nums) == 1:
        return

    # find pivot
    pivot = 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            pivot = i-1
            break

    # if reached the end, that means its the max perm so next perm is wrap around
    else:
        nums.reverse()
        return

    # find next value after pivot value to swap
    # sequence is ordered ascending right to left so we want to get the value where its no longer equal or less than the pivot
    swap = len(nums) - 1
    while nums[swap] <= nums[pivot]:
        swap-=1

    # swap
    nums[pivot], nums[swap] = nums[swap], nums[pivot]

    # sort the sequence
    reverse(nums, pivot+1, len(nums)-1)
    # nums[pivot+1:] = reversed(nums[pivot+1:])
    
    return nums


print("Expected Output: [1,4,1,2,3,3,5]")
print("Actual Output: ", nextPerm([1,3,5,4,3,2,1]))

print("Expected Output: [1,3,2]")
print("Actual Output: ", nextPerm([1,2,3]))



