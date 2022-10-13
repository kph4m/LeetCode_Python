"""
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Understand
- given grid of chars, return true if word exists in grid
    - connected horizontally or vertically

Match
- DFS

Plan
- created visited array to mark pos we already visited
- loop through rows
    - loop throguh columns
        - if dfs return true
            - return true

- return false

dfs helper function(board, word, cur_row, cur_col, visited, pos):
    if len of the word == pos, return true

    check if within bounds or board[cur_row][cur_col] == word[pos] or its already been visited

    visited = true

    check up, right, down, up positions

    if it doesnt end up being a path, set visited to false

    return true


Implement

Review

Evaluate
- Time Complexity: O(m*n*4^s), last grid might be the only valid grid, 3 choices for each char in word (don't count the one where we came from), where word is length s
- Space Complexity: O(m*n), visited dict that stores all values in the grid once, O(4^s) - recursion stack
"""

def exist(board, word):

    def dfs(board, word, cur_row, cur_col, pos, visited):
        # return True if pos reaches end of word
        if pos == len(word):
            return True

        # check bounds and if its the char of the word in the given position and if its been visited yet    
        if not (0 <= cur_row < len(board)) or not (0 <= cur_col < len(board[0])) or visited.get((cur_row, cur_col)) or board[cur_row][cur_col] != word[pos]:
            return False

        # set current position visited to true
        visited[(cur_row, cur_col)] = True

        # go through all directions
        res = dfs(board, word, cur_row + 1, cur_col, pos+1, visited) \
            or dfs(board, word, cur_row, cur_col+1, pos+1, visited) \
            or dfs(board, word, cur_row - 1, cur_col, pos+1, visited) \
            or dfs(board, word, cur_row, cur_col-1, pos+1, visited)

        # if cant find word in any of the directions, set False
        visited[(cur_row, cur_col)] = False

        return res


    # create visited dict
    visited = {}

    # loop through board to find 
    for cur_row in range(len(board)):
        for cur_col in range(len(board[0])):
            if dfs(board,word,cur_row, cur_col,0,visited):
                return True

    return False


print("Expected Output: True")
print("Actual Output:", exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

print("Expected Output: False")
print("Actual Output:", exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
