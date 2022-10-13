"""
Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Understand
- Tree: two nodes connected by one path (no cycles)
- return root label of min height tree
- [[2,3], [2,4], [1,3]

    2
   3 4   h = 2
  1   

    3
   2 1   h = 2
  4   

Both of them have same height so they're both min height trees -> return [2,3]
- can there be duplicate nodes?
    - all pairs are distinct
- always guaranteed to be connected?
    - yes
- if number of nodes <= 2
    - return those nodes
- there can only be a max of two roots that form a mht
    - even: (1) - (2) - (3) - (4)
        - mht of height 2 formed with roots 2 and 3
    - odd: (1) - (2) - (3)
        - mht of height 1 formed with root 2
    - hence, theres can only be a max of 2 roots that form mht

Match
- BFS

Plan
- Trim leaf nodes layer by layer until we reach the root nodes of the graph, those are the roots where there's a mht

- build adjacency list
- build queue to put all leaf nodes in
- trim out all leafs with each iteration and remove edges linked to the node until we get to only <=2 nodes left in the graph

Implement

Review
n = 4, edges = [[1,0],[1,2],[1,3]]

Adjacency List
0: 1
1: 0, 2, 3
2: 1
3: 1

queue = [0,2,3]

queue = [0,2]
0: 1
1: 0, 2
2: 1
3: 

queue = [0]
0: 1
1: 0, 
2: 
3: 
tmpQueue = [1]

queue = []
0: 
1:  
2: 
3: 
tmpQueue = [1]

return [1]

Evaluate
- Time Complexity: O(V), O(V)-1 to constructing the adjacency list given the edges, O(V) to find the initial nodes, trimming will take O(V + V - 1) to reach centroids
- Space Complexity: O(V), adjacency list is V nodes and V-1 edges, worse cases for queue is one level contains all leafs so V-1 
"""
from collections import defaultdict

def findMinHeight(n, edges):
    # edge case
    if n <= 2:
        return [i for i in range(n)]
    
    
    # create adjacency list
    neighbors = defaultdict(set)
    for u,v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
        
    # create queue and populate queue with inital leaves
    queue = [node for node in neighbors if len(neighbors[node]) == 1]
    
    # keep track of remaining nodes
    remaining_nodes = n
    
    # max roots for mht is 2
    while remaining_nodes > 2:
        remaining_nodes -= len(queue)
        
        # create temp cause we dont want to add the new leaf with the old leaves
        tmpQueue = []
        
        while queue:
            leaf = queue.pop()
            # remove neighbor of leaf
            neighbor = neighbors[leaf].pop()
            
            # remove leaf from neighbor
            neighbors[neighbor].remove(leaf)
            
            # append new nodes that are leaves
            if len(neighbors[neighbor]) == 1:
                tmpQueue.append(neighbor)
                
        queue = tmpQueue
                
    return queue


print("Expected Output: [1]")
print("Actual Output: ", findMinHeight(4, [[1,0], [1,2], [1,3]]))

print("Expected Output: [3,4]")
print("Actual Output: ", findMinHeight(6, [[3,0], [3,1], [3,2], [3,4], [5,4]]))