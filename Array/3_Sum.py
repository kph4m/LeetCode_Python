"""
3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Understand 
- Given an int array, return all possible triplets (can't be duplicates) that add up to 0
- [-1,0,1,2,-1,-4] -> [[-1,-1,2], [0,1,-1]]
- [1,1,1,-1,1] -> []
- [] -> []

Match
- Two Pointer

Plan

[-4, -1, -1, 0, 1 , 2]
  a   b             c

check every combination b and c with a
after you checked each one, increment a

- sort list to avoid duplicates
- create list to store triplets
- iterate through the sorted list, a is cur value, b and c are left and right pointers
    - skip duplicate value
    - assign left and right pointer
    - while l > right
        - calculate sum
        - if greater than 0, reduce by decrementing right pointer
        - if less than 0, increase by incrementing the left pointer
        - if it's equal to 0, append to list
            - shift left pointer (previous shifts will handle the rest) 
            - if its the same as the previous left value and left < right, keep incrementing
- return list

Implement

Review
[-1,0,1,2,-1,-4] 
[-4, -1, -1, 0, 1 , 2]
  a   b             c

[-4, -1, -1, 0, 1 , 2]
  a       b         c

[-4, -1, -1, 0, 1 , 2]
  a          b      c

[-4, -1, -1, 0, 1 , 2]
  a             b   c

[-4, -1, -1, 0, 1 , 2]     [[-1,-1,2]]
      a   b         c

[-4, -1, -1, 0, 1 , 2]
      a      b      c

[-4, -1, -1, 0, 1 , 2]   [[-1,-1,2], [-1,0,1]]
      a      b  c


[-4, -1, -1, 0, 1 , 2]   
             a  b   c

[-4, -1, -1, 0, 1 , 2]   
                a  b/c  

[-4, -1, -1, 0, 1 , 2]   
                    a/c  b


return [[-1,-1,2], [-1,0,1]]

Evaluate
- Time Complexity: O(nlogn) - sorting list + O(n^2) - double while loop = O(n^2)
- Space Complexity: O(1) - not using an data structures for the intermediate computations
"""

def threeSum(nums):

    triplets = []

    if not nums: 
        return triplets

    # sort list to easily handle duplicates: O(nlogn)
    nums.sort()

    for i, a in enumerate(nums):

        # skip duplicates for the a value
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums) - 1

        while l < r:
            
            # calc 3 sum
            threeSum = a + nums[l] + nums[r]

            # if less than 0, increment left pointer
            if threeSum < 0:
                l+=1

            # if greater than 0, decrement right pointer
            elif threeSum > 0:
                r-=1

            # if equal
            else:
                triplets.append([a, nums[l], nums[r]])

                # increment left to keep checking
                l+=1

                # skip duplicate values
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    return triplets


print("Expected Output: [[-1,-1,2], [-1,0,1]] ")
print("Actual Output: ", threeSum([-1,0,1,2,-1,-4]))

print("Expected Output: [] ")
print("Actual Output: ", threeSum([1,1,1,-1,1]))
            