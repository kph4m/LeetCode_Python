"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Understand
- anagram is you can rearrange the letters and it can become another word
- ajsh, jash, return True

Match
- String
- Dictionary

Plan
- Iterate through first string and store counter for each char
- Iterate through second string and if it's already in the dictionary, decrement
    - all values of the char should be 0 if it's an anagram
- iterate through all the values of the dictionary, if even one of them isn't 0, return false
- return true

Implement

Review 
- s = ajsh, t = jash
- Iterate through first string
    - counter = { a: 1, j: 1, s: 1, h: 1}
- Iterate through second string
    - counter = { a: 0, j: 0, s: 0, h: 0}
- Iterate through values of dict and check for non zero
    - All zero
- return True

Evalute
- Time Complexity: O(n)(iterate first string) + O(n)(iterate second string) + O(1)(iterate through max of 26 values - constant) = O(n)
- Space Complexity: O(1) - dictionary can contain a max of 26 entries from the alphabet
"""
def isAnagram(s,t):

    # check lengths for quick check
    if len(s) != len(t):
        return False

    counter = {}

    # store counter of all chars in s
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    # decrement counter for intersection of s and t, store unique chars
    for char in t:
        if char in counter:
            counter[char] -= 1
        else:
            counter[char] = 1
    
    # check if any value isn't 0 = not an anagram
    for value in counter.values():
        if value != 0:
            return False

    return True



"""
Alt Solution: using sorted function

Time Complexity: O(nlog(n)) from sorted function
Space Complexity: O(1)

def isAnagram(s,t):
    
    # check lengths
    if len(s) != len(t):
        return False

    # sort strings and check if they're equal
    return sorted(s) == sorted(t)
"""