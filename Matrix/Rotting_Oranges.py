"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Understand
- 0 - empty, 1 - fresh, 2 - rotten
- every min, 4 directional orange of a rotten become rotten
- find number of mins it takes for every orange to be rotten
    - if not possible, return -1
- is there only one rotten orange at the start or are there multiple?
- how do we account for disconnected oranges? (ones that arent connected 4-directionally)
    - traverse entire matrix and keep track of all fresh oranges

Match
- DFS
    - if there's only one starting rotten orange
- BFS
    - if there's multiple starting rotten oranges

Plan 
- if grid empty, return None
- create queue
- create variables for time and # of fresh oranges
- iterate through grid
    - if its a 1
        - increment fresh
    - if its a 2
        - append to the queue
- while q and theres fresh oranges in the graph
    - iterate through the initial fresh oranges in the q
        - pop the first orange
        - visit neighbors
            - if its not in bounds or its not a fresh orange, continue
            - mark it as rotten
            - append to queue
            - fresh -=1
    - increment time
        - the above loop made the neighbors of rotten ones rotten the first time
- return time if we went through every fresh orange else -1        

Implement

Review 
[
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

fresh = 6
q = [[0,0]]

q = [[0,1], [1,0]]
[
    [2,2,1],
    [2,1,0],
    [0,1,1]
]
fresh = 4
time = 1

q = [[1,0], [0,2], [1,1]]
[
    [2,2,2],
    [2,2,0],
    [0,1,1]
]
fresh = 2

q = [[0,2], [1,1]]
[
    [2,2,2],
    [2,2,0],
    [0,1,1]
]
fresh = 2
time = 2

q = [[2,1]]
[
    [2,2,2],
    [2,2,0],
    [0,2,1]
]
fresh = 1
time = 3

q = []
[
    [2,2,2],
    [2,2,0],
    [0,2,2]
]
fresh = 0
time = 4

return 4

Evaluate
- Time Complexity: O(n) - visit all the cells in the grid once
- Space Compelxity: O(n) - could possibly store all coordinates in the queue
"""
from collections import deque

def orangesRotting(grid):
    if len(grid) < 0:
        return -1
    
    q = deque()

    # time we'll be returning when all oranges rotten
    time = 0

    # keep track of fresh oranges 
    fresh = 0

    rows, cols = len(grid), len(grid[0])

    # iterate through entire grid to get # of fresh oranges and append rotting onces to queue
    for r in range(rows):
        for c in range(cols):
            # fresh
            if grid[r][c] == 1:
                fresh += 1
            # rotten
            if grid[r][c] == 2:
                q.append([r,c])

    
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    while fresh > 0 and q:

        # when this loops ends, thats one wave of infecting oranges, so increment time
        # visit a given round for the oranges
        for i in range(len(q)):
            r,c = q.popleft()

            # go through each neighbor
            for dr,dc in directions:
                row, col = dr + r, dc + c

                # check bounds and if its fresh
                if (
                    row in range(rows)
                    and col in range(cols)
                    and grid[row][col] == 1
                ):
                    # set to rotten
                    grid[row][col] = 2

                    # adds the next round of oranges to visit neighbors from
                    q.append([row,col])

                    # decrement fresh
                    fresh -= 1
        time += 1
    return time if fresh == 0 else -1
    

print("Expected Output: 4")
print("Actual Output: ", orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


print("Expected Output: -1")
print("Actual Output: ", orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))


print("Expected Output: 0")
print("Actual Output: ", orangesRotting([[0,2]]))