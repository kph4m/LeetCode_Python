"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Understand
- true if s can be segmented into words from dictionary
- "hellomyname", ["hello", "my", "name"] -> true
- no words in the dict are in s
    - return false
- "catsandog", ["cats", "dog", "sand", "and", "cat"] -> false
    - split cats -> andog, split and -> og, cant be split into any words
    - split cat -> sandog, split sand -> og, cant be split into any words


Match
- BFS
    - visited set = words we've visited
        - what strings we've already seen so we don't get caught in infinite cycle or reprocess things
    - queue = string after we split it using the words in the dict


Plan
        
        "catsandog"

     andog    sandog

    og            og


- create queue to store string after splits
- create visited to store words we've already processed to avoid unncessary processing
- put the initial string in the queue
- while queue exists
    - pop word from queue
    - if word already in visited, skip
    - else
        - if word is empty, we're able to split the string using the words so return true
        - add the word to visited
        - go through each word in dict, if the word starts with the word in the dict, append the split word to the queue

- if it never return true, can't fully segment word with the words in the dict, return false

Implement

Review
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

q = ["catsandog"]
visited = ()


q = ["andog", "sandog"]
visited = ("catsandog")

q = ["sandog", "og"]
visited = ("catsandog", "andog")

q = ["og", "og"]
visited = ("catsandog", "andog", "sandog")

q = ["og"]
visited = ("catsandog", "andog", "sandog", "og")

q= []
skip

Return false


Evaluate
- Time Complexity: O(n) - going through all words in word dict, O(n) - startwith, O(n) - splitting = O(n^3)
- Space Complexity: O(n) - queue, O(n) - set, O(n)

"""
from collections import deque

def wordBreak(s, wordDict):

    if not s or not wordDict:
        return False

    q = deque([s])

    visited = set()

    while q:
        word = q.popleft()

        if word in visited:
            continue

        else:
            if not word:
                return True

            visited.add(word)

            # leetcode
            # leet
            for words in wordDict:
                if word.startswith(words):
                    q.append(word[len(words):])
    
    return False

print("Expected Output: True")
print(wordBreak("applepenapple", ["apple", "pen"]))

print("Expected Output: False")
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))