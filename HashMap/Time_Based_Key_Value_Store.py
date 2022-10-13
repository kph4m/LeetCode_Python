"""
Time Based Key Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Understand
- TimeMap
    - key value that can store multiple values for the same key at different time stamps
    - foo: [[bar,1], [bar2, 4]]

- ["foo",1]
    - bar
- ["foo",4]
    - bar2
- ["foo",3]
    - bar
- set
    - stores key with value at given timestamp
- get
    - return value
    - multiple values
        - if time stamp doesnt exists, return value before it
        - no values, return ""
    - values are sorted by time everytime they're inserted
        - can perform get binary search for O(logn)

Match
- Dictionary

Plan
- init: dictionary
- set
    - check if already exists, if not set it
    - if exists, append it to list
- get
    - create string to return
    - get the list of the key
    - perform binary search


Implement

Review
- set("foo", "bar", 1)
    - foo: [["bar",1]]
- set("foo", "bar2", 4)
    - foo: [["bar",1], ["bar2", 4]]
- get("foo",5)
    - bar2

Evaluate
- init
    - Time Complexity: O(1)
    - Space Complexity: O(n) - dict
- set
    - Time Complexity: O(1)
    - Space Complexity: O(1)
- get
    - Time Complexity: O(logn) - binary search
    - Space Complexity: O(1)

"""

class TimeMap(object):

    def __init__(self):
        # key: [[value, timestamp]]
        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.store.get(key, [])

        l,r = 0, len(values) -1

        while l<=r:
            m = (l + r) # 2
            # assign to prev value
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            # move left
            else:
                r = m - 1

        return res


timeMap = TimeMap()
timeMap.set("foo", "bar", 1);         
print("Expected Output: bar")
print("Actual Output: ", timeMap.get("foo", 1));
print("Expected Output: bar")        
print("Actual Output: ",timeMap.get("foo", 3));         
timeMap.set("foo", "bar2", 4);
print("Expected Output: bar2")          
print("Actual Output: ", timeMap.get("foo", 4));
print("Expected Output: bar2")           
print("Actual Output: ", timeMap.get("foo", 5));         