"""
Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.


Understand
- find min bricks to cross if you ran a vertical line from first row to last row
- bruteforce - check every brick cut for each position and return the min
	- not efficient (what if the width was huge?)
- strat: find position with the most number of gaps
    - length of row - max number of gaps = min bricks to cross
- what if there are two with the same number?
    - shouldn't matter
- what if wall doesn't exist
    - return 0

Match
- Dictionary
    - key = position of gaps
    - val = number of gaps at that position
    - len(wall) - max(dict.values())

Plan
- if wall doesn't exist: return 0
- create dictionary
- iterate through rows
    - iterate through bricks
        - add gaps to dictionary
- return len(wall) - max(dict.values())

Implement

Review
wall = [[1,2,2,1], [3,1,2]]

countGap = {
    1: 1
    3: 2
    4: 1
    5: 1
}

return 2 - 2 = 0

Evaluate
- Time Complexity: O(m * n), going through each row and element
- Space Complexity: O(W), total width, worse case each brick width is 1

"""

def leastBricks(wall):

    if not wall:
        return 0

    countGap = {}

    for r in wall:
        total = 0
        # edge doesn't count
        for b in r[:-1]:
            total += b
            # add it to dict
            countGap[total] = 1 + countGap.get(total, 0)

    # possible to only have 1 brick for each row = no gaps
    if not countGap:
        return len(wall) - 0
    else:
        return len(wall) - max(countGap.values())

print("Expected Output: 2")
print("Actual Output: ", leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))


print("Expected Output: 0")
print("Actual Output: ", leastBricks([[1,2,2,1], [3,1,2]]))
