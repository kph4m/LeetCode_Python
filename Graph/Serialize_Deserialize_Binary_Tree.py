"""
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


Understand
- serialize binary tree
    - serialization: process of converting data strcuture or object into sequence of bits to be stored in file or transmitted across a network connection link to be reconstructed again
- serialize into string, deserialize back into binary tree

Match
- BFS (Level order traversal) or DFS (preorder)

Plan
- Serialize: convert binary tree into a string using preorder

     1
   2  3    -> "1,2,4,N,N,N,3,5,N,N,N"
  4  5

- Deserialize: convert string into a binary tree using preorder

                              1
"1,2,4,N,N,N,3,5,N,N,N" ->  2  3    
                           4  5


Implement


Review
   1
  2 3
 4 5 

["1","2","4","N","N","5","N","N","3","N","N"]
"1,2,4,N,N,5,N,N,3,N,N"

Serialize
res=[1,2,4,N,N,5,N,N,3,N,N]
return "1,2,4,N,N,5,N,N,3,N,N"

Deserialize
data = "1,2,4,N,N,5,N,N,3,N,N"
dataSplit = [1,2,4,N,N,5,N,N,3,N,N]

i = 0
node = 1
    i = 1
    node = 2
        i = 2
        node = 4
            i = 3
            node = Null
            i = 4
            node = Null
        i = 5
        node = 5
            i = 6
            node = Null
            i = 7
            node = Null
    i = 8
    node = 3
        i = 9
        node = Null
        i = 10
        node = Null
return TreeNode(1)

Evaluate
- Time Complexity: O(n) for serialize and deserialize, go through each element once
- Space Complexity: O(n), serialize array and deserialize recursive calls
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []
        
#         def dfs(node):
#             if not node:
#                 res.append("N")
#                 return
            
#             res.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)
            
#         dfs(root)
#         return ",".join(res)
        
        
#     # "1,2,4,N,N,5,N,N,3,N,N"
#     # ["1","2","4","N","N","5","N","N","3","N","N"]
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         dataSplit = data.split(",")
#         self.i = 0
        
#         def dfs():
#             if dataSplit[self.i] == "N":
#                 self.i+=1
#                 return
#             node = TreeNode(int(dataSplit[self.i]))
#             self.i+=1
#             node.left = dfs() 
#             node.right = dfs()
            
#             return node
        
#         return dfs()

def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    res = []
    
    def dfs(node):
        if not node:
            res.append("N")
            return
        
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    return ",".join(res)
    
    
# "1,2,4,N,N,5,N,N,3,N,N"
# ["1","2","4","N","N","5","N","N","3","N","N"]
def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    dataSplit = data.split(",")
    i = 0
    
    def dfs(i):
        if dataSplit[i] == "N":
            i+=1
            return
        node = TreeNode(int(dataSplit[i]))
        i+=1
        node.left = dfs(i) 
        node.right = dfs(i)
        
        return node
    
    return dfs(i)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Serialize
print("Expected Output: '1,2,4,N,N,5,N,N,3,N,N'")
result = serialize(root)
print("Actual Output: ", result)

# Deserialize
print("Expected Output: 1")
node = deserialize(result)
print("Actual Output: ", node.val)


