"""
Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Understand
- array represents asteroid in a row, number represents size of asteroid
- positive = right, negative = left
- if two asteroid collide, 
    - if one is greater, the smaller one explodes, leaving the greater one
    - if they're both equal, both of them explode
- [2, 5, -5, -1] -> [2,-1] -> [2]
- [-5, -2, 1, 8] -> [-5,-2,1,8] 
    - going in opposite directions
- [2,-5,3,4] -> [-5,3,4]
- [5,-2,3,-4] -> [5]
- [1,2,-3] -> [-3]

Match
- Stack

Plan
- create stack
- iterate through list 
    - while there are elements on the stack and it's going from positive to negative (colliding)
        - if they're both equal in magnitude, pop element in stack and skip to the next element
        - if stack element < current element, remove it and keep comparing it to the rest of the stack
        - if stack element > current elements, skip to next element
    - else, they're non-colliding elements (positive/positive, negative/negative, negative/positive) or stack has been completely destroyed so append current asteroid
- return stack

Implement

Review 
[5,-2,3,-4] -> [5]

add 5
output = [5]

abs(5) < abs(-2), skip to next asteroid

add 3
output = [5,3]

abs(3) < abs(-4), pop 3 from stack, continue comparison
abs(5) > abs(4), continue to next asteroid

return [5]

Evaluate
- Time Complexity: O(2n) -> O(n) - iterate through asteroid, worse case while loop [1,2,3,4,-5] popping off all values from stack
- Space Complexity: O(n) - stack that could hold max all input values ([1,2,3])
"""

def asteroidCollision(asteroids):

    output = []

    # iterate through asteroids
    for asteroid in asteroids:
        # collision condition: positive/negative and there are elements on the stack
        while output and output[-1] > 0 and asteroid < 0:

            # if they're equal in magnitude, explode both
            if abs(output[-1]) == abs(asteroid):
                output.pop()
                # move on to next asteroid since we're destroying top stack and current asteroid
                break

            # if stack < cur
            elif abs(output[-1]) < abs(asteroid):
                output.pop()

                # keep comparing with the current asteroid
                continue

            # if stack > cur
            elif abs(output[-1]) > abs(asteroid):
                # move on to next asteroid
                break

        # if it doesn't fit any of the collision reqs or stack is empty, add asteroid to stack
        else:
            output.append(asteroid)

    return output


print("Expected Output: [5]")
print("Actual Output: ", asteroidCollision([5,-2,3,-4]))

print("Expected Output: [-3]")
print("Actual Output: ", asteroidCollision([1,2,-3]))

