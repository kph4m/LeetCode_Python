"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Understand
nums = [1,4,6,3], target = 5 -> [0,1]
only one solution so don't have to worry about multiple different combinations
don't have to worry about empty array 

Match
Array traversal, calculate complement and store in dict

Plan
create dict which will store int as keys and indices as values
iterate through the list
  calculate the complement of the current int by target - current int
  if the complement exists in the dict, return current index and complement index
set dict[num] = i
return empty list if indices not found

Implement

Review
nums = [1,2,3], target = 4
i=0, num=1, comp = 3, intDict = { 1: 0}
i=1, num=2, comp = 2, intDict = { 1:0, 2:1, }
i=2, num=3, comp = 1, return [0,2]

Evaluate
Time Complexity: O(n) - go through each int in the list once
Space Complexity: O(n) - dict could be up to the size of the input
"""

def twoSum(nums, target):

    # Stores int as keys and index as value
    # Space Complexity: O(n)
    intDict = {}

    # Iterate over nums
    # Time Complexity: O(n)
    for i, num in enumerate(nums):

        # calculate the complement
        comp = target - num

        # check if complement exists in dict, if it is return current int index and comp index
        if comp in intDict:
            return [intDict[comp], i]

        # if comp not in dict, add current int to dict
        intDict[num] = i
    
    # return empty list if indices not found
    return []

nums = [1,2,3]
target = 4

# TEST
if __name__ == "__main__":
    print("Expected Output: [0,2]")
    print("Actual Output:", twoSum(nums,target))

    


