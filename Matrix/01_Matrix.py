"""
01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.


Understand
- given m x n matrix, return distance to get to a 0 for each cell
- [[0,0,0],[0,1,0],[0,0,0]] -> [[0,0,0],[0,1,0],[0,0,0]]

Match
- Matrix, BFS

Plan
Main Idea
- find all zero cells first
- start from these cells and perform bfs of their neighbors
- when visiting neighbors, calculate distance
- keep doing this untill all cells are visited


- create queue to store indexes of 0 values
- iterate through all elements by row
    - convert all 1's into infinity
    - add all 0's to queue
- create tuple with directions to visit the surrounding neighbors of a position
- iterate through queue, which contains 0 value positions
    - pop from the queue
    - calculate neighboring coordinates
    - make sure they're in bounds of the matrix
        - set the neighboring matrix to 1

Implement

Review
mat = [[0,0,0],[0,1,0],[1,1,1]]
- queue = [(0,0), (0,1), (0,2), (1,0), (1,2)]
- (0,0)
    - (1,0): 1
    - (-1,0): out of bounds
    - (0,1): 1
    - (0,-1): out of bounds
    - [(0,1), (0,2), (1,0), (1,2), (1,0), (0,1)]
- (0,1)
    - (1,1): 
    - (-1,1): out of bounds
    - (0,2)
    - (0,0)

Evaluate
"""

from collections import deque

def updateMatrix(mat):

    q = deque()

    for i, row in enumerate(mat):
        for j, el in enumerate(row):
            # if 0, append to q
            if mat[i][j] == 0:
                q.append((i,j))
            # if 1, set to infinity
            else:
                mat[i][j] = float('inf')

    # directions tuple: right,left,up,down
    directions = ((1,0), (-1,0), (0,1), (0,-1))

    while q:
        # for each element in the queue
        for ele in range(len(q)):

            # get the position of the first value in the queue
            i,j = q.popleft()

            # go through all neighbors
            for x,y in directions:
                row, col = i+x, j+y

                if -1 < row < len(mat) and -1 < col < len(mat[0]) and mat[row][col] > mat[i][j] + 1:
                    mat[row][col] = mat[i][j] + 1
                    q.append((row,col))

    return mat

