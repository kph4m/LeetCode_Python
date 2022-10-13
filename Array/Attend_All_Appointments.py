"""
Attend All Appointments

Given an array of intervals representing 'N' appointments, where each interval is an array of the form [start, end], return true if its possible to attend all appointments and false otherwise

Assume that if the end time of one appointment is the same as the start time of another appointment, it's possible to attend both (see last example)

Understand
- list of intervals
- return true if none of them overlap
- return false if one of them overlaps
- what if there's no intervals?
    - return True

Match
- interval traversal

Plan
- sort the intervals so its easier to figure out overlapping intervals
- create stack to store last visited interval
- push the first one onto the stack
- iterate through the intervals
    - pop the stack
    - if the start of the current interval is less than the end of the prev interval
        - overlap detected, return false
    - else, add the current interval to the stack
- return true

Implement

Review

Evaluate
- Time Complexity: O(nlogn) - sorting
- Space Complexity: O(1)? - max of 1 element in the stack at a given time 
"""
def canAttendAll(intervals):
    # Write your code here
    
    if not intervals:
        return True
    
    # sort intervals
    intervals.sort(key = lambda i: i[0])
    
    stack = []
    stack.append(intervals[0])
    
    for i,j in intervals[1:]:
        x,y = stack.pop()
        
        # overlap condition
        if i < y:
            return False
        stack.append([i,j])
    
    return True



print("Expected Output: False")
print("Actual Output: ", canAttendAll([[1,3], [3,5], [4,6]]))

print("Expected Output: True")
print("Actual Output: ", canAttendAll([[1,3], [3,5], [5,6]]))