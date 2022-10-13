"""
K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Understand
- Given array of points (x,y) and k, return k closest points to the origin (0,0)
    - can return the points in any order
- Distance is calculated by sqrt((x1-x2)^2 + (y1-y2)^2)
- [(-2,2), (1,3)]
    - sqrt((-2)^2 + (2)^2) = sqrt(8)
    - sqrt((1)^2 + (9)^2) = sqrt(10)
    - sqrt(8) < sqrt(10), closer
    - k = 1, return [[-2,2]]
- What if the distances are the same?
    - choose any one
- What if k > # of points?
    - return empty?
- What if there's duplicate points?
    - count the duplicates

Match
- List Traversal

Plan 1 - Use Dictionary
- create new list to store the result
- create a dictionary where the keys are the points and value are the distance from the origin
- iterate through array of points
    - calculate the distance from the origin, store in dictionary
- iterate through dictionary
    - while len(list) <= k
        - append the lowest distance point to the list
- return list
- Problem: Duplicate keys aren't allowed in dictionaries

Plan 2 - Use Heap
- create list for heap
- create list for the result we're going to return
- calculate the distance and store it in the list: (distance, x, y)
- heapify the list so its becomes structure of a heap
- start popping off the values and append it to the result

Implement

Review
[[3,3],[5,-1],[-2,4]], k = 2
- minHeap = [[sqrt(18),3,3], [sqrt(26),5,-1], [sqrt(20), -2, 4]]
- heapify: [[sqrt(18),3,3], [sqrt(20), -2, 4], [sqrt(26),5,-1]]
- while loop
    - k = 2, res = [[3,3]]
    - k = 1, res = [[3,3],[-2,4]]
    - k = 0, exit loop
- res = [[3,3], [-2,4]]

Evaluate

"""
# Implementation 1: Dictionary
# import math

# def kClosest(points,k):

#     if k > len(points):
#         return None

#     res = []

#     dict = {}

#     for point in points:

#         # calc the distance form the origin
#         distance = math.sqrt((point[0] + 0)**2 + (point[1] + 0)**2)

#         # store in dict
#         dict[tuple(point)] = distance

#     print(dict)

#     # sort dict by value
#     sortDict = sorted(dict.items(), key=lambda x: x[1])

#     print(sortDict)
    
#     for i in range(k):
#         res.append(list(sortDict[i][0]))

#     return res


# Implementation 2 - Heap

import math
import heapq

def kClosest(points,k):
    if k > len(points):
        return None

    res = []
    minHeap = []

    for x,y in points:
        distance = math.sqrt((x**2) + (y**2))
        minHeap.append([distance,x,y])

    # convert to heap
    heapq.heapify(minHeap)

    # start popping it off and appending to result
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k-=1
    
    return res

print("Expected Output: [[-2,2]]")
print("Actual Output", kClosest([[-2,2], [1,3]], 1))

print("Expected Output: [[3,3], [-2,4]]")
print("Actual Output", kClosest([[3,3],[5,-1],[-2,4]], 2))

# [[1,1],[2,2],[2,2],[2,-2]]
print("Expected Output: [[1,1],[2,2],[2,2],[2,-2]]")
print("Actual Output: ", kClosest([[2,2],[2,2],[3,3],[2,-2],[1,1]], 4))

        