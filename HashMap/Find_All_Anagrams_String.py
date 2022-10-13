"""
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Understand
- given string s and p, return  indices in s such that they start an anagram of string p
- s = skjwejksrn, p = skj, output: [0,5]
    - s = sjks, output = [0,1]?
- what if length of p > length of s?
    - no anagram possible, return []

Match
- Dict, Sliding Window

Plan
- Create dict with chars and freqs from p
- Create another dict for s
- Sliding window on s, dict only contains letters within the window (pop values if they're not in the window)
- if p dict and dict match, there's an anagram

Implement

Review

Evaluate
- Time Complexity: O(n) - go through element of the string once
- Space Complexity: O(1) - dicts can contains max 26 keys
"""

def findAnagram(s,p):
    if len(p) > len(s):
        return []

    sDict, pDict = {}, {}
    # create dict for s and p with len of p
    for i in range(len(p)):
        sDict[s[i]] = 1 + sDict.get(s[i],0)
        pDict[p[i]] = 1 + pDict.get(p[i],0)    

    # check if s and p equal, if they are add 0 to res, if not set empty
    res = [0] if sDict == pDict else []

    # set left pointer
    l = 0

    # iterate through from len(p) - len(s)
    for r in range(len(p), len(s)):
        # create new entry in dict
        sDict[s[r]] = 1 + sDict.get(s[r],0)

        # Prepare to move left pointer
        # remove freq from left counter since its no longer in the window
        sDict[s[l]] -= 1

        # check if freq 0, if it is, pop from dict
        if sDict[s[l]] == 0:
            sDict.pop(s[l])

        # increment left to change sliding window
        l+=1

        # check if dicts equal, if so append left pointer
        if sDict == pDict:
            res.append(l)

    return res


print("Expected Output: [0,6]")
print("Actual Output: ", findAnagram("cbaebabacd", "abc"))

print("Expected Output: [0,1]")
print("Actual Output: ", findAnagram("skjs", "skj"))

    




    