"""
Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Each node's value is the same as the index

Adjacency list
- set of neighbors of a node in the graph

Understand
- given adjacency list, return a deep copy (clone) of the graph
- graph is connected
- [[2,4],[1,3],[2,4],[1,3]] -> [[2,4],[1,3],[2,4],[1,3]]


Match
- DFS to go through each node and neighbor

Plan

Recursive DFS Implementation
- create dict where key is old node and new node
- perform dfs 
    - check if node is already in the dict
        - if not, that means a copy hasn't been created yet
    - create copy of old node and assign it in the dict
    - for neighbors in the old node
        - append them to the neighbors of the new node
    - return the copied node
- return dfs(node) 


BFS Implementation
- create queue, cloned node, dict: key - node, value - cloned node
- while q exists
    - pop current
    - for neighbors in current q
        - if neighbor isn't found in the dict
            - append neighbor to q
            - create cloned node
            - set it in the dict
        - append the neighbor as a neighbor for the cloned node
- return cloned[node]

Implement

Review 
Recursive Implementation - Too Confusing :(
[[2,4],[1,3],[2,4],[1,3]]
   1     2     3     4

dfs(1)
oldToNew: { Node1: Node1 }

    dfs(2): neighbors = 1,3
    oldToNew: { Node1: Node1, Node2: Node2 }

        dfs(1)
        return Node1

        dfs(3): neighbors = 2,4
        oldToNew: { Node1: Node1, Node2: Node2, Node3: Node3 }

            dfs(2)
            return Node2

            dfs(4): neighbors = 1,3
            oldToNew: { Node1: Node1, Node2: Node2, Node3: Node3, Node4:Node4 }


                dfs(1)
                return Node1

                dfs(3)
                return Node3

    dfs(4): neighbors = 1,3
    oldToNew: { Node1: Node1, Node2: Node2, Node4: Node4 }

        dfs(1)
        return Node1

        dfs(3)
        return Node3

BFS Implementation
[[2,4],[1,3],[2,4],[1,3]]
   1     2     3     4

queue = {Node1}, cloned = { Node1: Node1 }
queue = {Node2}, cloned = { Node1: Node1[Node2], Node2: Node2 }
queue = {Node2, Node4}, cloned = { Node1: Node1[Node2, Node4], Node2: Node2, Node4: Node4 }
queue = {Node4}, cloned = { Node1: Node1[Node2, Node4], Node2: Node2[Node1], Node4: Node4}
queue = {Node4, Node3}, cloned = { Node1: Node1[Node2, Node4], Node2: Node2[Node1, Node3], Node4: Node4, Node3: Node3}
queue = {Node3}, cloned = { Node1: Node1[Node2, Node4], Node2: Node2[Node1, Node3], Node4: Node4[Node1, Node3], Node3: Node3}
queue = {}, cloned = { Node1: Node1[Node2, Node4], Node2: Node2[Node1, Node3], Node4: Node4[Node1, Node3], Node3: Node3[Node2, Node4]}

return cloned[1] = Node1[Node2,Node4]

Evaluate
- Time Complexity: O(n) - number of Edges and vertices
- Space Complexity: O(n) - storing copies of all old nodes

"""

from collections import deque

def cloneGraph(node):

##### Recursive Implementationh #####

    # if not node:
    #     return None

    # oldToNew = {}

    # def dfs(node):
    #     # check if node exists in the dict, if it is return the copy
    #     if node in oldToNew:
    #         return oldToNew[node]

    #     # create the copy
    #     copy = Node(node.val)

    #     # put it in the dict
    #     oldToNew[node] = copy

    #     for nei in node.neighbors:
    #         copy.neighbors.append(dfs(nei))
        
    #     return copy
    
    # return dfs(node)


##### BFS Implementation #####

    if not node:
        return None

    # create cloned node
    cloned_node = Node(node.val)

    # create dict
    cloned = {}

    # add clone node to dict
    cloned[node] = cloned_node 

    queue = deque()
    queue.append(node)

    while queue:
        # get the top value from the queue
        cur = queue.popleft()

        # iterate through the neighbors of the node
        for neighbor in cur.neighbors:
            # if no neighbors
            if neighbor not in cloned:
                # add to queue
                queue.append(neighbor)
                # create clone
                cloned_neighbor = Node(neighbor.val)
                # add it to cloned
                cloned[neighbor] = cloned_neighbor
            # add cloned neighbor as a neighbor to the current node clone
            cloned[current].neighbors.append(cloned[neighbor])
    
    return cloned[node]
            





