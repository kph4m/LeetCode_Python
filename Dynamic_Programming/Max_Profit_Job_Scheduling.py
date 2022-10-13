"""
Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Understand
- given start and endtime array, and profit, return max profit such that no two jobs are overlapping
- is start time always in sorted order?

        [   30  ]
[   20  ][10][10]
1   2   3   4   5

Option 1: 20 + 10 + 10 = 40
Option 2: 20 + 30 = 50

Return 50


[(1,2,50), (2,4,10), (3,5,40), (3,6,70)]


Match
- Dynamic programming 

Plan
- sort jobs with start time
- for every job
    1. if selected, profit = profit [i] + next job after end
    2. else, profit = next job after start + 1
    3. max of 2 profit

- two choices
    - choose jobs[i]
        - profit at i + profit after i.endtime
    - skip jobs[i]
        - profit after i.starttime


N^2 solution
- jobs = combine the arrays and sort them by starting time for easier iteration
- N= len(startTime)
- create helper rec function
    - for jobs[i], there are two choices
        - don't pick i (i+1)
        - pick i
            - find next job where startTime >= arr[i].endTime to avoid time overlap
    - base case: if i==N, return 0 (no more )
    - j = i + 1 (will be the next job)
    - iterate through the array until reach a job that greater than current job at i (endtime[i] < startime[j])
    - first profit = jobs[i][2] + rec(j)
    - second profit = rec(i+1) (Skip i)
    - return max(first,second)
- rec(0)

Nlogn solution
- jobs = combine the arrays and sort them by starting time for easier iteration
- sort the startTime array to use for finding the job after job i
- N= len(startTime)
- create helper rec function
    - base case: if i==N, return 0 (no more )
    - j = bisect_left(startTime, jobs[i][1]) -    [1,2,4,5,5], endtime = 3
    - first profit = jobs[i][2] + rec(j)
    - second profit = rec(i+1) (Skip i)
    - return max(first,second)
- rec(0)

Implement

Review

Evaluate
Not using binary search
    - Time Complexity: O(n^2), going through each job, take O(n) to find next job
    - Space Complexity: O(n), recursive stack

Using binary search
    - Time Complexity: O(nlogn), going through each job, takes O(logn) to find next job
    - Space Complexity: O(n), recursive stack
"""
import bisect

def jobScheduling(startTime, endTime, profit):


    # O(n^2) approach

    n = len(startTime)
    # combine into single list
    jobs = sorted(list(zip(startTime,endTime,profit)))

    # dp
    def dp(i):

        # base case: reached end 
        if i == n:
            return 0
        
        # First choice: Don't pick i
        opt1 = dp(i+1)

        # Second choice: Pick i
        j = i + 1

        # Find the position where start time of j is greater than end time of i
        while j<n and jobs[i][1] > jobs[j][0]:
            j+=1

        opt2 = jobs[i][2] + dp(j)

        # return max of opt1 and opt2
        return max(opt1, opt2)

    return dp(0)


    # # O(nlogn) approach - using binary search using bisect to find j

    # n = len(startTime)
    # # combine into single list
    # jobs = sorted(list(zip(startTime,endTime, profit)))
    # startTime.sort()

    # # dp
    # def dp(i):

    #     # base case: reached end 
    #     if i == n:
    #         return
        
    #     # First choice: Don't pick i
    #     opt1 = dp(i+1)

    #     # Second choice: Pick i
    #     j = i + 1

    #     # Find the position where start time of j is greater than end time of i
    #     j = bisect.bisect_left(startTime, jobs[i][1])

    #     opt2 = jobs[i][2] + dp(j)

    #     # return max of opt1 and opt2
    #     return max(opt1, opt2)

    # dp(0)


print("Expected Output: 120")
print("Actual Output: ", jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))

print("Expected Output: 150")
print("Actual Output: ", jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))