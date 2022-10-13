"""
Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Understand
- Starting from the pixel image [sr][sc], perform flood fill with the color to the tiles that are 4 directionally of the starting pixel, and 4 directional to those tiles.

Match
- Lists, DFS

Plan
- Base Cases: 
    - Index out of bound
    - current position isn't the same color as the starting position
- Edge Cases:
    - List is none
    - Starting position already same color
    - Return image if any of these cases apply
- Use dfs to recursively fill in all the colors of up, down, left, right positions 


Implement

Review

Evaluate
Recursive Approach
- Time Complexity: O(n), where n is the total amount of pixels
- Space Complexity: O(n), where n is the size of the call stack when calling the recursive function
"""

def floodFill(image, sr, sc, color):

########### Recursive Approach ####################

#     # Edge Cases
#     # List doesn't exist or same color as color
#     if image is None or image[sr][sc] == color:
#         return image

#     # call recursive dfs function
#     fill(image, sr,sc, image[sr][sc], color)

#     # return image afterwards
#     return image

# def fill(image, sr, sc, oldColor, newColor):

#     width = len(image)
#     height = len(image[0])

#     # Base Cases
#     # Out of bounds for row and column, check if newColor doesn't match the old color (so can't modify it)
#     if sr < 0 or sr >= width or sc < 0 or sc >= height or oldColor != image[sr][sc]:
#         return

#     # assign new color to position
#     image[sr][sc] = newColor
    
#     # right
#     fill(image, sr, sc+1, oldColor, newColor)

#     # left
#     fill(image, sr, sc-1, oldColor, newColor)

#     # down
#     fill(image, sr-1, sc, oldColor, newColor)

#     # up
#     fill(image, sr+1, sc, oldColor, newColor)


################  Recursive Approach v2  #################

    # # get row and column length
    # row, column = len(image), len(image[0])
    
    # # old color to compare later
    # old = image[sr][sc]
    
    # # if the starting color is the same as the new color, skip
    # if old == color:
    #     return image
    
    # def dfs(r, c):
    #     # if cell is old color
    #     if image[r][c] == old:
    #         # replace with new color
    #         image[r][c] = color
            
    #         # up
    #         if r >= 1: dfs(r-1, c)
            
    #         # down
    #         if r+1 < row: dfs(r+1, c)
                
    #         # left
    #         if c >= 1: dfs(r, c-1)
                
    #         # right
    #         if c+1 < column: dfs(r, c+1)

    # dfs(sr, sc)
    # return image


############# DFS STACK APPROACH ################

    # old color to compare later
    old=image[sr][sc]

    # if the starting color is the same as the new color, skip
    if old == color:
        return image

    # add the first cell to the stack
    stack=[(sr,sc)]

    # get length of row and column
    row = len(image)

    column = len(image[0])

    # while stack not empty
    while(stack):
        
        # pop the first value
        i,j=stack.pop()

        # if a cell isn't the new color
        if(image[i][j]==old):

        # change it to the new color
            image[i][j]=color    

            # Check all 4 directions and make sure they're in bounds

            if(i+1<row):
                stack.append((i+1,j))
            if(i-1>=0):
                stack.append((i-1,j))
            if(j+1<column):
                stack.append((i,j+1))
            if(j-1>=0):
                stack.append((i,j-1))

        # if a cell is already the new color, skip it
        else:
            continue
    return image

print("Expected Output: ",[[0,0,0],[0,0,0]])
print("Actual Output: ", floodFill([[0,0,0],[0,0,0]], 0,0,0))

print("Expected Output: ",[[2,2,2],[2,2,0],[2,0,1]])
print("Actual Output: ", floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
