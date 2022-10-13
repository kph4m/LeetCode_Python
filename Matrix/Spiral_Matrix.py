"""
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Understanding
- Given matrix, return elements in spiral order

[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[1,2,3,6,9,8,7,4,5]

Match
- List traversal

Plan
- create top, bottom, left, right boundaries
- once we finish going through a boundary, we adjust them to make the traversal submatrix smaller
- we know we traversed all positions if TB overlap or LR overlap.

Implement

Review

[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


left = 0, right = 3, top = 0, bottom = 3
output = [1,2,3]
top = 1
output = [1,2,3,6,9]
right = 2

0 < 2, 0 < 3, keep going

output = [1,2,3,6,9,8,7]
bottom = 2
output = [1,2,3,6,9,8,7,4]
left = 1

1 < 2, 1 < 2, keep going

output = [1,2,3,6,9,8,7,4,5]
top = 2

right = 1

1 !< 1, 2 !< 2, break

return [1,2,3,6,9,8,7,4,5]

Evaluate
- Time Complexity: O(m*n) - traversed through entire matrix
- Space Complexity: O(m*n) - output with all grid elements

"""
def spiralMatrix(matrix):
    output = []

    # intial positions
    left,right = 0, len(matrix[0])
    top,bottom = 0, len(matrix)

    while left < right and top < bottom:
        # go through top row
        for i in range(left,right):
            output.append(matrix[top][i])
        top += 1

        # go through right column
        for i in range(top,bottom):
            output.append(matrix[i][right-1])
        right -= 1

        # if its 1 dimensional for column, then we traversed all of it
        if not (left < right or top < bottom):
            break

        # go through bottom row
        for i in range(right-1, left-1,-1):
            output.append(matrix[bottom-1][i])
        bottom-=1

        # go through left column
        for i in range(bottom-1, top-1, -1):
            output.append(matrix[i][left])
        left +=1


    return output


print("Expected Output: [1,2,3,6,9,8,7,4,5]")
print("Actual Output: ", spiralMatrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))

print("Expected Output: [1,2,3,4,8,12,11,10,9,5,6,7]")
print("Actual Output: ", spiralMatrix([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]))