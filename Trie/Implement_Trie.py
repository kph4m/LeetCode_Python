"""
Implement Trie

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Understand
- Trie: tree where each letter of a word is a Node
- the last char of a word is marked
- insert apple
    - (a) -> (p) -> (p) -> (l) -> (e - end)
- search apple
    - True
- starts with (app)
    - True

Match
- Trie
- Dictionary for Children

Plan
- create TrieNode 
    - children: dictionary
        - 'a': { 'p': TrieNode() }, 'p': { 'p': TrieNode()}, 'p': { 'l': TrieNode()}, 'l': { 'e': TrieNode()}, 'e': {}
    - if its an end node: boolean
- init
    - create empty root TrieNode
- insert
    - set cur to root node
    - iterate through each char in word to be inserted
        - if it's not part of the node children, create new TrieNode and add it to dict
        - move the cur to the current character
    - set the last char as an end node
- search
    - set cur to root node
    - iterate through each char in word to be searched
        - if it's not part of the children, return false
        - move cur to the current char
    - when reach the last char, check if its the last one
- startWith
    - set cur to root node
    - iterate through each char in word to be searched
        - if its not part of the children, return false
        - move cur to the current char
    - return True

Implement

Review
- insert('apple')
    - (a) -> (p) -> (p) -> (l) -> (e - end)
        - children: 'a': { 'p': TrieNode() }, 'p': { 'p': TrieNode()}, 'p': { 'l': TrieNode()}, 'l': { 'e': TrieNode()}, 'e': {}
- search('appl')
    - l doesn't have end set to true, return false
- startsWith('app')
    - has a, p, p
    - return true

Evaluate
- TrieNode
    - Init:
        - Time Complexity: O(1)
        - Space Complexity: O(n)
- Trie
    - Init:
        - Time Complexity: O(1)
        - Space Complexity: O(n)
    - insert
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    - search
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    - startsWith
        - Time Complexity: O(n)
        - Space Complexity: O(1)
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


trie = Trie();
trie.insert("apple");
print("Expected Output: True")
print("Actual Output: ", trie.search("apple"));   

print("Expected Output: False")
print("Actual Output: ", trie.search("app"));

print("Expected Output: True")
print("Actual Output: ",trie.startsWith("app")); 

trie.insert("app");
print("Expected Output: True")
print("Actual Output: ", trie.search("app"));     