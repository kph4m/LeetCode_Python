"""
Size of Submatrix

You're given a 2D matric that is filled with 1's in almost all the cells. Howerver, there may be at most one rectangular submatrix that is filled with 0s. Implement an algorithm to retunr the size of the submatrix, in terms of width and height.

Understand
- given 2d matrix, there might be a rectangular submatrix
- return dimensions of the submatrix in an array

Match
- DFS (stack)

Plan

To get width and height of submatrix
- (2,2), (2,3), (2,4)
- (3,2), (3,3), (3,4)

width = max(y) - min(y) + 1
    - 4 -2 + 1 = 3

height = max(x) - min(x) + 1
    - 3 - 2 + 1 = 2

- create list to store all coordinates]
    - calculate width and height later
- create stack
- add first value to stack
- while stack not empty:
    - pop from stack
    - if it's a 0
        - 
    - for each neighbor of c
        - add to the stack
"""

def findSubmatrix(matrix):
    # Write your code here
    
    coords = []
    stack = []
    
    row = len(matrix)
    col = len(matrix[0])
    
    stack.append([0,0])
    
    while stack:
        i,j = stack.pop()
        
        # if its a 0, add coords to coord
        if matrix[0][0] != 0:
            continue
        else:
            coords.append([i,j])
        
        if i + 1 < row:
            stack.append((i+1, j))
            
        if i - 1 >= 0:
            stack.append((i-1, j))
            
        if j + 1 < col:
            stack.append((i, j+1))
            
        if j - 1 >= 0:
            stack.append((i, j-1))
            
    print(coords)
    
    coords.sort(key = lambda i: i[0])
    
    width = coords[len(coords)-1][1] - coords[0][1]
    height = coords[len(coords)-1][0] - coords[0][0]
    
    return [width, height]