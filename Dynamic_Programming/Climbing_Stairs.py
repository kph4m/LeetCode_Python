"""
Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Understand
- return the number of distinct ways, using 1 or 2 steps, for n
- n = 3
    - 1,2
    - 1,1,1
    - 2,1
- return 3

Match

Plan
- bottom-up dynamic programming
    - calculate the number of ways starting from the bottom (n)
    - use the previously calculated subproblem steps to solve the current ones
        - i.e. add the number of steps from 5->5 and 4->5 to solve steps for 3->5
            - 5->5: 1, 4->5: 1, 3->5: 1+1 = 2, 2->5: 3, 1->5: 5, 0->5: 8
    - since the values only depend on 2 values, just use 2 variables to store the values instead of storing all the elements
    - this works because we're only using 1 and 2

Implement

Review
n = 5
- 0: curStep = 2, prevStep = 1
- 1: curStep = 3, prevStep = 2
- 2: curStep = 5, prevStep = 3
- 3: curStep = 8, prevStep = 5
- 4: curStep = 13, prevStep = 8

Evaluate
- Time Complexity: O(n) - going through all elements from 0 to n-1
- Space Complexity: O(1)

"""

def climbStairs(n):

    if not n:
        return 0

    curStep, prevStep = 1,1

    for i in range(n-1):
        temp = curStep
        curStep = curStep + prevStep
        prevStep = temp
    return curStep



