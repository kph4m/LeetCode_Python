"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Understand
- each row, column, and subbox can only have unique values to be valid
    - if duplicate, not valid

board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

False, column 1 contains 2 eights, square 1 also has 2 eights


Match
- HashMap (Dict)

Plan
- go through row, check if there any duplicates using length and set
- go through column, check if there any duplicates using length and set
- go through subboxes iterating in increments of 3 for row and column, use a set to store visited values
    - create a helper method to go through each subbox


Implement

Review
board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Each row doesn't have a duplicate
Col one has a duplicate, return False


board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Each row doesn't have a duplicate
Each col doesn't have a duplicate
Subbox 1 has 2 eights, return False


Evaluate
- Time Complexity: O(9^2), double for loop
- Space Complexity: O(9^2) if we're considering auxillary space, creating array for each row and col, creating set for each subbox

"""

def isValidSudoku(board):

    # row
    for r in range(9):
        # go through each row and store all non-period values
        row = [c for c in board[r] if c != "."]
        # check if length of original and unique are the same
        if len(row) != len(set(row)): return False
        

    # column
    for c in range(9):
        # go through each col and store all non-period values
        col = [board[r][c] for r in range(9) if board[r][c] != "."]
        # check if length of original and unique are the same
        if len(col) != len(set(col)): return False


    # iterate through each subbox
    def helper(R,C):
        visited = set()
        for r in range(R, R+3):
            for c in range(C, C+3):
                if board[r][c] == ".": continue
                elif board[r][c] not in visited: visited.add(board[r][c])
                else: return False

        return True


    # iterate through each beginning of subbox
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            if not helper(r,c): return False 

    return True


print("Expected Output: False")
print("Actual Output: ", isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print("Expected Output: False")
print("Actual Output: ", isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print("Expected Output: True")
print("Actual Output: ", isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","4",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))