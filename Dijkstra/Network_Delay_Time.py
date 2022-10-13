"""
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


Understand
- return min time takes for all nodes to receive signal
    - return the greatest time it takes for signal to pass to a node
- graph: times[source, target, time it takes for signal to travel from source to target]

Match
- Dijkstra - find shortest path between two vertices, do this from k to all nodes

Plan
- create adjacency list, storing (dest, weight) for each node
- create max path length to get to once node
- perform bfs and record the max path length
    - use minheap to pop min path length from queue
- return t if all nodes have been visited, else return -1


Implement

Review
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
graph = {2: [(1,1), (3,1)], 3: [(4,1)]}

minHeap = [(0,2)]

minHeap = []
maxT = 0
visited = (2)
minHeap = [(1,1),(1,3)]

minHeap = [(1,3)]
maxT = 1
visited = (2,1)
minHeap = [(1,3)]


minHeap = []
maxT = 1
visited = (2,1,3)
minHeap = [(1,4)]

minHeap = []
maxT = 2
visited = (2,1,3,4)
minHeap = []

return 2

Evaluate
- Time Complexity: O(N + ElogN), goes through each node (N), logN for heappop operation, doing that for each edge in the queue
- Space Complexity: O(N+E), build adjacency list is E, queue can store up to N elements
"""
from collections import defaultdict
import heapq

def networkDelayTime(times, n, k):

    # Create adjacency list
    graph = defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))


    # Create minheap - serves as queue
    minHeap = [(0,k)]

    # Visited set to avoid cycles
    visited = set()

    # Max time to get to a node - we'll return this
    maxT = 0

    # BFS
    while minHeap:
        time1, start = heapq.heappop(minHeap)

        if start in visited:
            continue

        visited.add(start)

        maxT = max(time1, maxT)

        for dest,time2 in graph[start]:
            if v not in visited:
                heapq.heappush(minHeap, (time2+time1,dest))

    return maxT if len(visited) == n else -1


print("Expected Output: 2")
print("Actual Output: ", networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))

print("Expected Output: 1")
print("Actual Output: ", networkDelayTime([[1,2,1]],2,1))