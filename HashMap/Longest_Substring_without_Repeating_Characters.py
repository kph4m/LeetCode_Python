"""
Longest Substring without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Understand
- given string, find length of substring such that no repeating characters occur
- "abcjsa" = "abcjs" = 5
- "sabsjfa" = "absjf" = 5
- "aaaa" = "a" = 1
- "" = 0

Match
- Sliding Window

Plan
- check if string is empty
- create dictionary where keys are chars and values are index the char was last seen
- create start pointer
- create maxLength
- enumerate through string
    - if char is found in dict, set the start to max(start, last occurrence index + 1)
    - set max length to max(maxLength, r-l + 1)
    - set the index occurence of the character
- return length

Implement

Review
"abcbsa"
- start = 0, end = 0, char_index = {}, maxLength = 0
- start = 0, end = 0, maxLength = 1, char_index = {a: 0}
- start = 0, end = 1, maxLength = 2, char_index = {a:0, b:1}
- start = 0, end = 2, maxLength = 3, char_index = {a:0, b:1, c:2}
- b in char_index, start = 2, end = 3, maxLength = 3, char_index = {a:0, b:3, c:2}
- start = 2, end = 4, maxLength = 3, char_index = {a:0, b:3, c:3, s:4}
- a in char_index, start = 2, end = 5, maxLength = 4, char_index = {a:5, b:3, c:3, s:4}
- return 4

Evaluate
- Time Complexity: O(n) - go through all the strings in the input
- Space Complexity: O(1) - dictionary limited to 26 chars
"""

def lengthofLongestSubstring(s):

    if not s:
        return 0

    char_index = {}
    maxLength = 0
    start = 0

    for end, char in enumerate(s):
        # if duplicate found
        # set start to the last occurence + 1 
        if char in char_index:
            start = max(start, char_index[char] + 1)

        # update max length
        maxLength = max(maxLength, end - start + 1)

        # set the occurence of the char in the dict
        char_index[char] = end
    
    return maxLength


print("Expected Output: 4")
print("Actual Output: ", lengthofLongestSubstring("abcbsa"))

print("Expected Output: 3")
print("Actual Output: ", lengthofLongestSubstring("pwwkew"))

print("Expected Output: 1")
print("Actual Output: ", lengthofLongestSubstring("aaa"))