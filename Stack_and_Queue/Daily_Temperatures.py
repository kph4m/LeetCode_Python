"""
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Understand
- given array temps, return array answer such that answer[i] is the number of days you have to wait after ith day to get warmer temp
- [43,30,34,56,32]
    - [3,1,1,0,0]
- equal values?
    - not greater

Match
-  Monotonic stack (top -> bottom is decreasing)

Plan
- create array with inital values 0 with length of temps array
- iterate through temps
    - append index, temp to stack
    - if we find a temp day greater than the top of the stack, pop the value, subtract the current day with the day from the stack and assign it to return array
    - keep popping values if current temp is more than those in the array

Implement

Review
- [43,30,34,56,32]
- answer = [0,0,0,0,0]
- stack = [(0,43)]
- stack = [(0,43), (1,30)]
- stack = [(0,43), (0,34)], answer = [0,1,0,0,0]
- stack = [(3,56)], answer = [3,1,1,0,0]
- stack = [(3,56), (4,32)], answer = [3,1,1,0,0]
- return answer = [3,1,1,0,0]

Evaluate
- Time Complexity: O(n) - going through each element in temps once
- Space Complexity: O(n) - worse case (decreasing temp array) stack is the size of the temp array
"""

def dailyTemperatures(temperatures):
    if not temperatures:
        return []
        
    answer = [0] * len(temperatures)

    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            idx, tempVal = stack.pop()
            answer[idx] = i - idx
        stack.append((i,temp))
    return answer


print("Expected Output: [3,1,1,0,0]")
print("Actual Output: ", dailyTemperatures([43,30,34,56,32]))

print("Expected Output: [1,1,1,0]")
print("Actual Output: ", dailyTemperatures([30,40,50,60]))

print("Expected Output: [1,1,0]")
print("Actual Output: ", dailyTemperatures([30,60,90]))

print("Expected Output: [8,1,5,4,3,2,1,1,0,0]")
print("Actual Output: ", dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))



