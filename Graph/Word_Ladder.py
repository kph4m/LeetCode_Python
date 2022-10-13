"""
Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


Understand
- given beginWord and endWord and dicrtionary wordList, return number of words in shortest transformation sequence, 0 if not such sequence exists
    - each adjacent word in sequence has one letter change
- are we guaranteed that the wordList has the words to go from beginWord to endWord?
- cat   dog   [cat, dat, dot, dog, log, dug]
    - 4 (cat -> dat -> dot -> dog)
- hit cog ["hot","dot","dog","lot","log","cog"]
    - hit 
        -> *it = []
        -> h*t = [hot]
        -> hi* = []

        - hot
            -> *ot = [dot,lot]
            -> h*t
            -> ho*

            - dot
                -> *ot 
                -> d*t
                -> do* = [dog]

                - dog
                    -> *og = [cog]
                    -> d*g
                    -> do* = 

            - lot
                -> *ot = 
                -> l*t
                -> lo* = [log]

                - log
                    -> *og = [cog]
                    -> l*g
                    -> lo* = 
        

    - 5 ("hit" -> "hot" -> "dot" -> "dog" -> cog")
    - 5 ("hit" -> "hot" -> "lot" -> "log" -> log")

Match
- Shortest Sequence = BFS

Plan
- create a dictionary where the keys are the transforms of each word
    - {"*ot": [hot], "h*t": [hot], "ho*": [hot]}
- maintain visited so no cycle
- create deque which will contain: word, distance
- use bfs
    - if popped word is the same as end word, return distance
    - go through each char and transform it for the word
        - if the transformed words are in the dictionary, append each word to the queue so we 

Implement

Review

Evaluate
- Time Complexity: O(n*m^2) - creating the transformDict, O(n*m^2) - queue, creating the transform word
- Space Complexity: O(n*m^2) - m^2 possible transforms, go through each word
"""

from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    if beginWord == endWord or not wordList or endWord not in wordList:
        return 0
    
    # Creating the transform dict
    # {"*ot": [hot], "h*t": [hot], "ho*": [hot]}
    
    transformDict = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            transform = word[:i] + "*" + word[i+1:]
            transformDict[transform].append(word)
            
    
    # Create queue
    queue = deque([(beginWord,1)])
    
    # Create visited
    visited = set()
    
    # BFS
    while queue:
        word, distance = queue.popleft()
        
        if word == endWord:
            return distance
        
        visited.add(word)
        
        
        # Create transforms for word and see if it matches in the transformDict
        for i in range(len(word)):
            transform = word[:i] + "*" + word[i+1:]
            
            potential_words = transformDict.get(transform, None)
            
            if potential_words:
                for potential_word in potential_words:
                    if potential_word not in visited:
                        queue.append((potential_word, distance+1))
                                
    return 0

print("Expected Output: 4")
print("Actual Output: ", ladderLength("cat", "dog",["dat", "dot", "dog", "log", "dug"] ))

print("Expected Output: 5")
print("Actual Output: ", ladderLength("hit", "cog",["hot","dot","dog","lot","log","cog"] ))

