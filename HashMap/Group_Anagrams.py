"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Understand
- given an array of string, group the anagrams together in their own array

- Input: ["cat", "tac", "act", "bot", "tob", "lob"]
- Output: [["cat", "tac", "act"], ["bot", "tob"], ["lob"]]

- Input: [""]
- Output: [[""]]

- Are there uppercase letters?
    - No

Match
- HashMap, Counter

Plan
- loop through array
- sort all the words
- add them to hashmap where key = sorted word and value is an array of all the words that are anagrams

OR 

For python, use Counter to see if two strings have the same count for letters

Implement

Review

[['cat', 'tac', 'act'], ['bot', 'tob'], ['lob']]
anagramDict = {act: ['cat', 'tac', 'act'], bot: ['bot', 'tob'], lob: ['lob']}

Evaluate
- Time Complexity: O(n) - first loop
- Space Complexity: O(n) - worse case, no anagrams so it'll fill up the dictionary with the input size

"""
from collections import Counter
from collections import defaultdict

def groupAnagrams(arr):

    # Timed Out Solution
    # arrCopy = arr.copy()
    # arrResult = []

    # # Outer loop for words
    # for word in arr:
    #     tempArr = []
    #     newArrCopy = arrCopy.copy()
    #     for wordArr in newArrCopy: 
    #         # if they're anagrams
    #         if Counter(word) == Counter(wordArr):
    #             # print(wordArr, Counter(word) == Counter(wordArr))
    #             tempArr.append(wordArr)
    #             arrCopy.remove(wordArr)
    #     if not tempArr: 
    #         continue
    #     arrResult.append(tempArr)

    # return arrResult


    # Optimal Solution

    # Create dict with list as values
    anagramDict = defaultdict(list)

    for word in arr:
        key = str(sorted(word))
        anagramDict[key].append(word)

    return list(anagramDict.values())

print("Expected Output: [['cat', 'tac', 'act'], ['bot', 'tob'], ['lob']]")
print("Actual Output: ", groupAnagrams(["cat", "tac", "act", "bot", "tob", "lob"]))

print("Expected Output: [['bat'],['nat','tan'],['ate','eat','tea']]")
print("Actual Output: ", groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

print("Expected Output: [['']]")
print("Actual Output: ", groupAnagrams(['']))

print("Expected Output: [['a']]")
print("Actual Output: ", groupAnagrams(['a']))


