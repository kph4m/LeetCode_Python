"""
Integer Replacement

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2. If n is odd, replace n with either n + 1 or n - 1. Return the minimum number of operations needed for n to become 1.

Understand
- find out the minimum number of operations needed for n to become 1 with the follorwing operations
    - if n is even, replace n with n/2
    - if n is odd, replace n with either n+1 or n-1
- 8
    - 8 -> 4 -> 2 -> 1
    - 3 operations
- 7
    - 7 -> 8 -> 4 -> 2 -> 1
    - 4 operations 
- 13
    - 13 -> 12 -> 6 -> 3 -> 2 -> 1
    - 5 operations
    - 13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1
    - 6 operations

Match
- Recursion or While loop

Plan

Naive
- if even
    - divide by 2
- if odd
    - check if n+1 or n-1 is even
        - if even, divide by 2
        - if odd, add 1
- keep track of operations
- repeat
- return operations

Optimal
- if even
    - divide by 2
- if odd
    - how do we determine if +1 or -1 is more optimal? modulo 4 to view ahead
        - check if n+1 or n-1 % 4 == 0, choose the one that has a remainder of 0, which will guarantee the next two operations will be even, which is more optimal
        - base case: if n == 3, return n-1 so it goes to 2 -> 1 instead of 4 -> 2 -> 1
- keep track of operations
- repeat
- return operations

Implement

Review

Evaluate
"""

# Naive While Solution - doesn't account for all cases
# Time Complexity: O(logn)
# Space Complexity: O(1)
# def integerReplacement(n):
#     operations = 0
#     while n != 1:
#         # if even
#         if n % 2 == 0:
#             n = n // 2
#         # if odd
#         else:
#             # check if n+1 or n-1 is even
#             if (n+1) % 2 == 0:
#                 n = n + 1
#             else:
#                 n = n - 1
#         operations += 1
#     return operations


# Optimal While Solution
# Time Complexity: O(logn)
# Space Complexity: O(1)
# def integerReplacement(n):
#     operations = 0
#     while n != 1:
#         # if even
#         if n % 2 == 0:
#             n = n // 2
#         # if odd
#         else:
#             # check if n+1 or n-1 is even
#             if (n+1) % 4 == 0 and n != 3:
#                 n = n + 1
#             else:
#                 n = n - 1
#         operations += 1
#     return operations

# Optimal Recursive Solution
# Time Complexity: O(logn)
# Space Complexity: O(n)
def integerReplacement(n):
    # base case
    if n == 1:
        return 0
    # if even
    if n % 2 == 0:
        return 1 + integerReplacement(n // 2)
    # if odd
    else:
        # check if n+1 or n-1 is even
        if (n+1) % 4 == 0 and n != 3:
            return 1 + integerReplacement(n + 1)
        else:
            return 1 + integerReplacement(n - 1)


## Optimal Memoization Solution
# Time Complexity: O(logn)
# Space Complexity: O(logn)
def integerReplacement(n):
    memo = {}
    def helper(n):
        # base case
        if n == 1:
            return 0
        # if even
        if n % 2 == 0:
            if n in memo:
                print(memo)
                return memo[n]
            else:
                memo[n] = 1 + helper(n // 2)
                print(memo)
                return memo[n]
        # if odd
        else:
            if n in memo:
                print(memo)
                return memo[n]
                
            else:
                if (n+1) % 4 == 0 and n != 3:
                    memo[n] = 1 + helper(n + 1)
                    print(memo)
                    return memo[n]
                else:
                    memo[n] = 1 + helper(n - 1)
                    print(memo)
                    return memo[n]
    
    return helper(n)

print("Expected Output: 3")
print("Actual Output:", integerReplacement(8))

print("Expected Output: 4")
print("Actual Output:", integerReplacement(7))

print("Expected Output: 5")
print("Actual Output:", integerReplacement(13))