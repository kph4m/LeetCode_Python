"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Understand
- LRU (Least Recently Used) Cache
    - init
        - positive size capacity
    - get
        - value of key
        - return -1 if doesn't exist
    - put
        - update value of key if key exists
        - otherwise add key-value pair to cache
        - if number of keys exceeds the capacity, evict the least recently used key

Match
- Dictionary, Deque
- Deque: [LRU - Recently Used]

Plan
- init
    - Dictionary to store key and value pairs
    - Deque to keep track of LRU element
- get
    - check if its exists or not
    - if it does, remove old one and add a new one so its recently used
- put
    - if it exists, remove it
    - if capacity is exceeded, remove LRU from deque and remove it from dictionary
    - append to deque
    - add to dict

Implement

Review


Stores keys and values
dict = {}

Contains Keys, LRU = front, RU = back
deque = []

put 1,1

dict = {1: 1}
deque = [1]

put 2,2

dict = {1: 1, 2:2}
deque = [1,2]

get 1

dict = {1:1, 2:2}
deque = [2,1]
return 1

put 3,3

dict = {1:1, 3:3}
deque = [1,3]

put 4,4

dict = {3:3, 4:4}
deque = [3,4]

Evaluate
- Time Complexity: O(n) - remove
- Space Complexity: O(n) - n is the max capacity
"""
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        # create dict to store values
        self.dict = {}
        self.deque = deque()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # if doesnt exist in dict, return -1
        if key not in self.dict:
            return -1

        # remove and reappend so its recent 
        self.deque.remove(key)
        self.deque.append(key)

        return self.dict[key]
    
    def put(self, key: int, value: int) -> None:
        # check if key in dict, remove if so
        if key in self.dict:
            self.dict.remove(key)
        
        elif len(self.deque) == self.capacity:
            # remove lru from deque
            value = self.deque.popleft()

            # remove lru value form dictionary
            self.dict.remove(value)

        self.deque.append(key)
        self.dict[key] = value


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)