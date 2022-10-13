"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.


Understand
- given s and t, return min substring of s that contains all chars (including dups) of t
- s = "akhdffb", t= "bffd" -> "dffb"

Match
- Substring = Sliding Window

Plan
- Expand the subwindow until it has all desired characters, then reduce the window as much as possible while retaining the desired chars

-left, right pointer
- right expands until we get desirable window
    - expand left while maintaining desirable window
    - if not desirable anymore, repeat

Implement

Review
s="ADBCKA", t="ABC"

countT = {"A": 1, "B": 1, "C": 1}
start, end = 0
targetLen = 3

end = 0
targetLen = 2
countT = {"A": 0, "B": 1, "C": 1}

end = 1
targetLen = 2
countT = {"A": 0, "B": 1, "C": 1, "D":-1}

end = 2
targetLen = 1
countT = {"A": 0, "B": 0, "C": 1, "D":-1}

end = 3
targetLen = 0
countT = {"A": 0, "B": 0, "C": 0, "D":-1}
minWindow = "ADBC"
countT = {"A": 1, "B": 0, "C": 0, "D":-1}
targetLen = 1 (remove A from window)
start = 1

end = 4
targetLen = 1
countT = {"A": 1, "B": 0, "C": 0, "D":-1, "K":1}

end = 5
targetLen = 0
countT = {"A": 0, "B": 0, "C": 0, "D":-1, "K":1}

return minWindow = "ADBC"

Evaluate
- Time Complexity: O(len(s)+len(t)), in the worse case, might have to visit each element twice (through start and end pointer)
- Space Complexity: O(len(s)+len(t)), when the window size is equal to entire string, when T has all unique chars
"""
from collections import Counter

def minWindow(s,t):

    if not s or not t:
        return ""

    # create dict out of t
    countT = Counter(t)

    # set pointers to first 
    start,end = 0,0

    # string that'll contain minwindow
    minWindow = ""

    # keep track of target length, which will be used to see if we got all letters in the target
    targetLen = len(t)

    # iterate through s
    for end in range(len(s)):

        # When see a target letter, decrease target len
        # Doing this beforehand, we don't decrease target len if we encounter it another time
        if countT[s[end]] > 0:
            targetLen -= 1

        # decrease the letter from the target count
        countT[s[end]] -= 1


        # when all letters are found
        while targetLen == 0:

            # calc the len of current window
            lenWin = end - start + 1

            # if there's no minwindow or it is lower than current min window, replace it
            if not minWindow or lenWin < len(minWindow):
                minWindow = s[start:end+1]

            # increase letter count of current letter
            countT[s[start]] += 1

            # account for if a non-target has been countered -> one of the target characters that we use to validate the target is now out of the window
            if countT[s[start]] > 0:
                targetLen += 1

            start+=1
    return minWindow


print("Expected Output: dffb")
print("Actual Output: ", minWindow("akhdffb", "bffd"))

print("Expected Output: ABDC")
print("Actual Output: ", minWindow("ADBCKA", "ABC"))