"""
Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Understand
- given array of non overlapping intervals and new interval, insert new interval into intervals such that they still dont have overlapping intervals (merge overlapping intervals when necessary), return intervals
- [[1,5], [8,10]], newIntervals = [6,7]
    - [[1,5], [6,7],[8,10]]
- [[1,5], [6,10]], newIntervals = [4,7]
    - [[1,5], [6,10]]

Match
- List of lists, merging intervals

Plan
- create result variable to construct new interval to return
- iterate through all intervals
- Check if new interval conflict with any intervals
    - it conflicts if the end of new interval isn't less than start of interval or start of new interval isn't greater than current interval
    - if it doesn't conflict, just append it
- merging:
    - create new interval with min num and max num
    - don't add it, as the new interval can conflict with other intervals

Implement

Review
[[1,3],[6,9]], newInterval = [2,5]
- [1,3], [2,5]
    - doesn't fit the 2 conditions, overlapping
    - newInterval = [1,5]
- [6,9] [1,5]
    - 5 (newInterval[1]) < 6 (intervals[i][0])
    - output = [[1,5]]
    - return [[1,5]] + [[6,9]] = [[1,5], [6,9]] 

Evaluate
- Time Complexity: O(n) - iterate through all intervals in the list
- Space Complexity: O(n) - output array could possibly have n intervals 


"""

def insert(intervals, newInterval):

    output = []

    # iterate through all intervals
    for i in range(len(intervals)):

        # NON-OVERLAPPING Conditions
        # if it can go before cur interval, append it and return output + all intervals
        # if its the first one, we can assume it won't overlap with next intervals
        if newInterval[1] < intervals[i][0]:
            output.append(newInterval)
            return output + intervals[i:]

        # if it can go after cur interval, append it
        # don't return yet cause it can overlap with next intervals
        elif newInterval[0] > intervals[i][1]:
            output.append(intervals[i])

        # OVERLAPPING Condition - merge new interval with cur interval
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    output.append(newInterval)
    return output


print("Expected Output: [[1,5], [6,9]]")
print("Actual Output: ", insert([[1,3],[6,9]],[2,5]))

print("Expected Output: [[1,2], [3,5], [6,9]]")
print("Actual Output: ", insert([[3,5], [6,9]],[1,2]))

print("Expected Output: [[1,9]]")
print("Actual Output: ", insert([[1,3],[4,9]],[2,5]))

