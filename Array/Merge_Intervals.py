"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Understand
- given array of intervals, merge the ones that are overlapping
- return array of non-overlapping intervals that cover all the intervals in the input
- [[1,4], [2,3], [5,9], [6,10]]
    - [[1,4],[5,10]]
- is it always going to be sorted?

Match
- Array Traversal

Plan
- sort the array by the first value
- create res array to return
- iterate through intervals array
    - compare end of most recent added interval with the cur end interval
    - if the prev interval end is greater than or equal to the start of the cur interval (overlapping condition)
        - set prev interval end to max(prev end, cur end)
    - else (not overlapping)
        - append to output
- return output

Implement

Review
[[1,3],[2,6],[8,10],[15,18]]
res = [[1,3]]
3 > 2, max(3,6) -> 6. [[1,6]]
6 !> 8, [[1,6], [8,10]]
10 !> 15, [[1,6], [8,10], [15,18]]
return [[1,6], [8,10], [15,18]]

Evaluate
- Time Complexity: O(nlog(n)) - sorting 
- Space Complexity: O(n) - res could contain same number of intervals in the worse case
"""

def merge(intervals):

    if not intervals:
        return None
    
    # sort by the start interval value
    intervals.sort(key = lambda i: i[0])

    # res array to return 
    res = []

    # add the first interval
    res.append(intervals[0])

    # iterate through intervals
    for start, end in intervals[1:]:

        # overlap condition: cur start <= prev end
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)

        else:
            res.append([start,end])
    
    return res


print("Expected Output: [[1,6],[8,10],[15,18]]")
print("Actual Output: ", merge([[1,3],[2,6],[8,10],[15,18]]))

print("Expected Output: [[1,5]]")
print("Actual Output: ", merge([[1,4],[4,5]]))