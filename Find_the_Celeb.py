"""
Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know them but they do not know any of them.

Goal: You want to find out who the celebrity is or verify that there is not one.

Output: The number associated with the celebrity, or -1 if no celebrity present.

You are given a helper function knows(a, b)-->bool which tells you whether A knows B.

Implement a function findCelebrity(n)-->int, your function should minimize the number of calls to knows(a, b).


Understand
- celebrity: everyone knows them, they know no one
- n people, n-1 people know the celebrity
- celebrity does not know anyone
- return the number associated with the celebrity, 0r -1 if no celebrity present
- example: n=3
    - 0,1,2
    - 0 knows 1, 0 knows 2, 1 knows 2, 2 knows no one
    - 2 is the celebrity


Match

Plan

Review
0 1 2
0 knows 1, 0 knows 2, 1 knows 2, 2 knows no one

i=0
isCelebrity(0, 3)
    j=0
    i!=j and (knows(0,0) or not knows(0,0)) - skip
    j=1
    return False

i=1
isCelebrity(1, 3)
    j=0
    i!=j and (knows(1,0) or not knows(0,1)) - skip
    j=1 - skip
    j=2
    i!=j and (knows(1,2) or not knows(2,1))
    return False

i=2
isCelebrity(2, 3)
    j=0
    i!=j and (knows(2,0) or not knows(0,2)) - skip
    j=1
    i!=j and (knows(2,1) or not knows(1,2)) - skip
    j=2 - skip
    return True

return 2

Evaluate

"""
# Not Optimal
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# def findCelebrity(n):
#     # iterate through all people
#     for i in range(n):
#         # if i is a celebrity
#         if isCelebrity(i, n):
#             # return i
#             return i
#     # if no celebrity, return -1
#     return -1

# # helper function to check if i is a celebrity
# def isCelebrity(i, n):
#     # iterate through all people
#     for j in range(n):
#         # if i knows j, or j doesn't know i
#         if i != j and (knows(i, j) or not knows(j, i)):
#             # return false
#             return False
#     # return true
#     return True


# Optimal - find the candidate first, then check if they are a celebrity
# Time Complexity: O(n)
# Space Complexity: O(1)
def findCelebrity(n):
    # set candidate to 0
    candidate = 0
    # iterate through all people
    for i in range(1, n):
        # if candidate knows i
        if knows(candidate, i):
            # set candidate to i
            candidate = i
    # check if candidate is a celebrity
    if isCelebrity(candidate, n):
        # return candidate
        return candidate
    # if no celebrity, return -1
    return -1

# helper function to check if i is a celebrity
def isCelebrity(i, n):
    # iterate through all people
    for j in range(n):
        # if i knows j, or j doesn't know i
        if i != j and (knows(i, j) or not knows(j, i)):
            # return false
            return False
    # return true
    return True