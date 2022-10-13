"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


Understand
- gas array = how much gas is at each station
- cost array = how much gas it takes to get to the next station
- return the index of the starting station if you can travel around the circuit once in the clockwise direction
- if there is no solution, return -1
- Is there guaranteed to be a solution?
    - Yes
- Is the array always going to be the same length?
    - Yes
- Is the array always going to be positive integers?
    - Yes
- Is the array always going to be integers?
    - Yes
- Is the array always going to be non-empty?
    - Yes
- gas = [1,2,3,4,5]
- cost = [3,4,5,1,2]
- 0 -> 1 = 3 gas
    - can't start here since we only have 1 gas and it takes 3 gas to get to the next station
- 1 -> 2 = 4 gas
    - can't start here since we only have 2 gas and it takes 4 gas to get to the next station
- 2 -> 3 = 5 gas
    - can't start here since we only have 3 gas and it takes 5 gas to get to the next station
- 3 -> 4 = 1 gas (start at the fourth gas station)
    - can start here since we have 4 gas and it only takes 1 gas to get to the next station
- 4 -> 0 = 2 gas

Match

Plan
- keep track of the current gas and the total gas (total gas is the sum of all the gas, if its negative by the end, then there is no solution), starting point
- Iterate through the gas array
    - total gas += gas[i] - cost[i]
    - current gas += gas[i] - cost[i]
    - if gas(i) - cost(i) is less than 0
        - reset the current gas to 0
        - set the starting station to the next station
- return the starting station if total gas is greater than or equal to 0 (there is a solution) else return -1

Implement

Review
gas = [2,3,4], cost = [3,4,3]

2 - 3 < 0, cant go to first station
totalgas = -1, currentgas = 0, startingPoint=1
3 - 4 < 0, cant go to second station
totalgas = -2, currentgas = 0, startingPoint = 2
4 - 3 >= 0, can go to third station
totalgas = -1, currentgas = 1, startingPoint = 3

totalgas = -1, its negative when we went through the entire array so no solution so return -1


Evaluate
- Time Complexity: O(n), go through each of the gas stations once
- Space Complexity: O(1), only need to keep track of the current gas and total gas
"""

def canCompleteCircuit(gas, cost):
    if len(gas) < 1:
        if gas[0] - cost[0] >= 0:
            return 0
        else:
            return -1
        
    totalGas = currentGas = startingPoint = 0 
    
    for i in range(len(gas)):
        curGas = gas[i] - cost[i]
        totalGas += curGas
        currentGas += curGas
        
        if currentGas < 0:
            startingPoint = i + 1
            currentGas = 0
            
    return startingPoint if totalGas >= 0 else -1

print("Expected Output: 3")
print("Actual Output: ", canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print("Expected Output: -1")
print("Actual Output: ", canCompleteCircuit([2,3,4], [3,4,3]))

