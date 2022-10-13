"""
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Understand
- given 
    - numCourses (how many courses to take)
    - prerequisites (list of lists that looks like [a,b])
        - have to take course b in order to take course a
- return true if you can finish all the courses
- numCourses = 2, prerequisites = [[1,0],[0,1]]
    - 0 -> 1, 1-> 0, produces a cycle, can't complete any courses

Match
- DFS

Plan
- create adjacency list for each course that has their pre-reqs using dict
- check all courses and their prerequisites using DFS and make sure they're able to be completed (no cycles)
- to check for cycles, create set and keep track of all visited nodes

Implement

Review
numCourses = 5, prereqs = [[0,1], [0,2], [1,3], [1,4], [3,4]]

adjList = { 0: [1,2], 1: [3,4], 2: [], 3: [4], 4: []}
visited = (0,1,3,4)
visited = (0,1,3)
visited = (0,1,3,4)
visited = (0,1,3)
visited = (0,1)
visited = (0,2)
visited = (0)
visited = (1)
visited = (2)
visited = (3)
visited = (4)

0: return True
    1: return True
        3: return True
            4: no prereqs, return True
        4: return True
    2: no prereqs, return True
1: return True
2: return True
3: return True
4: return True

adjList = { 0: [], 1: [], 2: [], 3: [], 4: []}
visited = ()

Evaluate
- Time Complexity: O(n + p), where n is the courses and p are the prerequisites
- Space Complexity: O(n + p), where n is the courses and p are the prerequisites

"""

def canFinish(numCourses, prerequisites):

    # CREATE ADJACENCY LIST

    # Create empty dict for each value in numCourses
    adjList = { i:[] for i in range(numCourses)}

    # Adds prereqs to each course
    for crs, prereq in prerequisites:
        adjList[crs].append(prereq)

    # Create set that'll track each visited node in the dfs path
    visited = set()

    # Dfs function
    def dfs(crs):

        # Check if its in the visit set, return False if so
        if crs in visited:
            return False

        # Check if it has any prereqs, if not return True
        if adjList[crs] == []:
            return True

        visited.add(crs)


        # Go through each prereq and perform DFS on it
        for prereq in adjList[crs]:
            # If its false, its in the visited, return False
            if not dfs(prereq):
                return False
        
        # After going through the paths, remove course visited
        visited.remove(crs)


        # At this point, we know the courses will be able to be completed
            # Set their prereqs to empty to skip DFS work
        adjList[crs] = []

        return True
    
    # Call Dfs on each course
    for course in adjList:
        if not dfs(course):
            return False
    
    return True


print("Expected Output: False")
print("Actual Output: ", canFinish(2, [[1,0],[0,1]]))

print("Expected Output: True")
print("Actual Output: ", canFinish(2, [[1,0]]))

print("Expected Output: True")
print("Actual Output: ", canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))

    
