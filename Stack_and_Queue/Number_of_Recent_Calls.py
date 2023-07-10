"""
Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.

int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Understand
- return the number of requests that have happened in the inclusive range [t - 3000, t]
- t is in milliseconds
- Example
    - ping(1) --> 1
    - ping(100) --> 2
    - ping(3001) --> 3
    - ping(3002) --> 3

Match
- Queue

Plan
- requests = []
- ping(t)
    - append t to requests
    - while requests in the list are less than t - 3000
        - remove from list starting from the beginning
    - return the length of the requests


Implement

Review

Evaluate
- Time Complexity: O(n) - worse case, pop everything in the list
- Space Complexity: O(n) - worse case, list will contain all the requests
"""
class RecentCounter:

    def __init__(self):
        self.requests = []
    
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)
    
obj = RecentCounter()
print("Expected Output: 1")
print("Actual Output: ", obj.ping(1))

print("Expected Output: 2")
print("Actual Output: ", obj.ping(100))

print("Expected Output: 3")
print("Actual Output: ", obj.ping(3001))

print("Expected Output: 3")
print("Actual Output: ", obj.ping(3002))