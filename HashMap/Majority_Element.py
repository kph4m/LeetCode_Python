"""
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Understand
- return the majority element, the element that appears more than n/2 times
- will always exist in the array
- [1,4,4,2,4,4] -> 4

Match
- List

Plan
- iterate through array, finding the occurences for each element
- check the occurrences, if its more than n/2, return the key

Implement

Review

Evaluate
"""

from collections import Counter

def majorityElement(nums):
    
    if not nums:
        return None

    thres = len(nums) / 2

    counter = Counter(nums)

    for key,val in counter.items():
        if val > thres:
            return key

print("Expected Output: ", 4)
print("Actual Output: ", majorityElement([1,4,4,2,4,4]))
