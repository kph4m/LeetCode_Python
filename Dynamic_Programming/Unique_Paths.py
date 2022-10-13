"""
Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Understand
- robot at starting position 0,0
- finish at m-1, n-1
- find number of possible unique paths 
- can only go right or down at a time

Match
- Dynamic Programming, DFS


Plan
- go through each path using DFS
- add the unique paths at each step

Implement

Review
[s][][]
[][][e]

first right:
    - down
        - right
            - reach, return 1
        - down
            - out of bounds, return 0
        - return 1 + 0 = 1
    - right
        - down
            - reach, return 1
        - right
            - out of bounds, return 0
        - return 1 + 0 = 1
    - return 1 + 1 = 2

first down
    - down
        - out of bounds, return 0
    - right
        - down
            - out of bounds, return 0
        - right
            - reach, return 1
        - return 0 + 1 = 1
    - return 0 + 1 = 1

return 2 + 1 = 3

Evaluate
- Time Complexity: O(m*n) - go through each grid in the matrix
- Space Complexity: O(m*n) - maintain dp
"""

# Bruteforce Approach
# Time Complexity: 2^(m+n), each grid has 2 options to go right or down, this will compound
# Space Complexity: O(m+n), recursive stack
def uniquePath(m,n):
    def dfs(i,j):
        if i >= m or j >= n:
            return 0
        if i == m-1 and j == n-1:
            return 1
        return dfs(i+1,j) + dfs(i,j+1)
    return dfs(0,0)


# Memoization Approach
def uniquePaths(m,n):

    dp = [[0]*n for i in range(m)]

    def dfs(dp,i,j):
        # if its out of bounds
        if i > m - 1 or j > n - 1:
            return 0
        # if its reaches the end
        if i == m-1 and j == n-1:
            return 1
        # if its already calculated, return
        if dp[i][j]:
            return dp[i][j]
        # store ways to get to dest for each grid pos so dont have to recalculate it (memoization)
        dp[i][j] = dfs(dp,i+1, j) + dfs(dp,i, j+1)
        print(dp)
        return dfs(dp,i+1, j) + dfs(dp,i, j+1)
    return dfs(dp,0,0)


print("Expected Output: 28")
print("Actual Output: ", uniquePaths(3,7))

print("Expected Output: 3")
print("Actual Output: ", uniquePaths(3,2))