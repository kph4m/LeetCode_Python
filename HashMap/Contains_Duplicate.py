"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Understand
- return true if any value appears at least twice
- return false if any value appears only once
- [1,2,4,5,2] = true
- [1,2,3] = false

Match
- List, Dictionary to store frequencies of ints

Plan
- create dictionary to store ints as keys and frequencies as values
- iterate through the dict
    - if any value is 2 or greater, return false
- return true

Implement

Review
[1,2,4,4]
- create dict of frequencies
    - { 1: 1, 2: 1, 4: 2}
- iterate through values
    - 4 occurs 2 times, return True

Evaluate
- Time Complexity: O(n) - create dict and iterate through dict values
- Space Complexity: O(n) - create dict of n elements

"""

from collections import Counter

def containsDuplicate(nums):
    counter = Counter(nums)

    for val in counter.values():
        if val >= 2:
            return True
    
    return False