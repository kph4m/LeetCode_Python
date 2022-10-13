"""
First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Understand:
- given a list of n versions and a method isBadVersion that determines if a version is bad, find the first bad version

Match
- List

Plan
- perform binary search
- create left and right pointer
- while left < right
    - cal mid
    - if mid is bad version
        - it could either be the start or previous elements could be the start
        - include mid in the search so set right to mid
    - if its not bad version
        - the first bad version must be after mid
        - set left to mid + 1
- return right / left, doesn't matter cause they'll be pointing to the same thing at the end of the while loop
        
Implement

Review
- [1,2,3,4,5], 5 is first bad
- mid = 3, not bad, left = 4, right = 5
- mid = 4, not bad, left = 5, right = 5
- return 5

Evaluate
- Time Complexity: O(logn) - skip elements that dont' fit criteria, binary search
- Space Complexity: O(1)

"""

def badFirstVersion(n):

    left,right = 0, n

    while left < right:
        # find mid
        mid = (left + right) // 2 

        # if mid is bad, it could be first or prev els could be first
        # include it in the next search
        if isBadVersion(mid):
            right = mid
        # if mid not bad, first bad has to be after mid
        # don't include it in search
        else:
            left = mid + 1
    return right