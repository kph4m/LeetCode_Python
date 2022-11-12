"""
Get Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold.

Understand
- Find the path that will have the max sum
- Can only do one step in left, right, down, up
- Can't visit a 0 cell

Input = [[0,6,0],
         [5,8,7],
         [0,9,0]]

Output = 9 -> 8 -> 7 = 24

Input = [[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]

Output = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 = 

Match
- DFS

Plan
- iterate through the grid, call dfs on all values that are >0
- find max path from each starting point, save max sum

Implement

Review
Input = [[0,6,0],
         [5,8,7],
         [0,9,0]]

Start at 6
- go to 8
- max((6,8,7), (6,8,5) , (6,8,9)) = 23

Start at 5
- go to 8
- max((5,8,7), (5,8,6) , (5,8,9)) = 22

Start at 8
- max((8,7), (8,6) , (8,9), (8,5)) = 17

Start at 7
- go to 8
- max((7,8,9), (7,8,5) , (7,8,6)) = 24

Start at 9
- go to 8
- max((9,8,7), (9,8,6) , (9,8,5)) = 24

Return 24

Evaluate
- Time Complexity: O((n*m) * 3^(n*m)), iterate through entire grid and calling dfs which we can visit up to 3 neighbors (excluding the origin point)
- Space Complexity: O(n*m), dfs stack depth can be up to the size of the grid

"""
def getMaximumGold(grid):

    maxGold = 0
    row = len(grid)
    col = len(grid[0])

    def dfs(i,j):
        gold = grid[i][j]

        # assign it 0 so u don't visit it again
        grid[i][j] = 0
        result = 0

        # go through each direction and get the max sum from the directions
        for x,y in [(i+1, j), (i-1,j), (i, j+1), (i,j-1)]:
            if 0 <= x < row and 0 <= y < col and grid[x][y] > 0:
                result = max(result, dfs(x,y))

        # assign it back to the original value to do dfs with other origin points
        grid[i][j] = gold
        return result + gold

    for i in range(row):
        for j in range(col):
            maxGold = max(maxGold, dfs(i,j))
    return maxGold


print("Expected Output: ", 24)
print("Actual Output: ", getMaximumGold([[0,6,0],
         [5,8,7],
         [0,9,0]]))


print("Expected Output: ", 28)
print("Actual Output: ", getMaximumGold([[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]))



    





        