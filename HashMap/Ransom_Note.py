"""
Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Understand
- Return true if magazine consists of letters that can construct ransomNote
- ransomNote = "sjdn", magazine= = "ndjssjk", return True
- ransomNote = "asd", magazine = "", return False

Match
- List
- Dictionary to store occurences

Plan
- create dict for storing all chars in the magazine and their occurences
- iterate through entire magazine
    - if it exists in the dict, +1 occurence
    - else, = 1 occurence
- iterate through entire ransom note
    - if its not found in the dict or occurence is 0, return false
    - if its found in the magazine dict, -1 occurence
- return true

Implement

Review
ransomNote = "sjdn", magazine= = "ndjssjk"
- mDict = { n: 1, d: 1, j: 2, s: 2, k:1 }
- Iterate through ransomNote
    - mDict = {n: 0, d: 0, j:1, s:1, k: 1}
- return True

Evaluate
- Time Complexity: O(m+n) - iterate all chars of magazine, iterate through ransom note
- Space Complexity: O(m) - all elements in magazine
"""

def canConstruct(ransomNote, magazine):

    if not ransomNote or not magazine:
        return False
    
    mDict = {}

    # iterate through all chars in magazine and store their occurences
    for char in magazine:
        # if exists, increment occurence
        if char in mDict:
            mDict[char] +=1
        # doesn't exist, set as 1
        else:
            mDict[char] = 1
    
    # check all chars in ransomeNote if they exist in magazine
    for ch in ransomNote:
        if ch not in mDict or mDict[ch] == 0:
            return False
        else:
            mDict[ch] -= 1
    
    return True
        