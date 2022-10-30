"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Understand
- find numbers of islands (1's connected horizontally or vertically)
    - diagonals don't count
- ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    - 1
- ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
    - 3
- empty grid
    - return 0

Match
- DFS or BFS

Plan

- if empty
    - return 0
- create islands variable to keep track of # of islands
- iterate through rows and columns
    - if its a 1, call dfs(r,c,grid) (or bfs(r,c)) to traverse neighbors
    - increment islands when dfs is finished
- return islands

- DFS(r,c,grid)
    - Base Case (to stop recursion):
        - if r and c aren't in bounds or isn't equal to 1, return
    - mark as visited (0)
    - call recursive function on other neighbors

- BFS(r,c,grid)
    - create queue
    - add coordinates to queue
    - set coordinates to '0', indicating it's been visited
    - while queue
        - pop right value from queue
        - create directions to go through each neighbor
        - loop through directions
            - create new r and new c from directions
            - if its valid (within bounds) and = 1
                - append it to the queue
                - set it to visited


Implement

Review

Evaluate
DFS
- Time Complexity: O(m*n), go through each of the grid positions once
- Space Complexity: O(m*n), worse case, whole grid filled with land

BFS
- Time Complexity: O(m*n), go through each of the grid positions once
- Space Complexity: O(min(m,n)), worse case, whole grid filled with land and queue will have max elements of the lesser of the two
"""

from collections import deque

def numIslands(grid):

    # Edge case
    if len(grid) < 1:
        return 0
    
    islands = 0

    rows = len(grid)
    cols = len(grid[0])

    def bfs(r,c,grid):
        queue = deque()
        queue.append((r,c))
        grid[r][c] = '0'

        while queue:
            r, c = queue.popleft()
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == '1':
                    queue.append((newR, newC))
                    grid[newR][newC] = '0'

    # Go through each cell
    for i in range(rows):
        for j in range(cols):
            # if its a 1, go through neighbors
            if grid[i][j] == '1':
                bfs(i,j,grid)
                # increment when dfs call returns, indicating an island
                islands += 1
    return islands


# def dfs(r,c,grid):
#     # Base Case: return if not in bounds or not a 1
#     if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
#         return
    
#     # Set as visited
#     grid[r][c] = '0'

#     # Recursive calls on neighbors
#     dfs(r+1, c, grid)
#     dfs(r-1, c, grid)
#     dfs(r, c+1, grid)
#     dfs(r, c-1, grid)


print("Expected Output: 1")
print("Actual Output: ", numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print("Expected Output: 3")
print("Actual Output: ", numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

                
