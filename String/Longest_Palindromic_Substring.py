"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Understand
- given string, find the longest palindromic substring
- palindrome = word that can be read forwards and backwards
    - racecar, bob
- skshahsksd -> skshahsks
- what if there's two palindromes of the same length?
    - return any of them
- two types of palindromes that can be found
    - odd length: aba
    - even length: cbbc
- no string?
    - return ""

Match
- Two Pointer

Plan
- iterate through the string
    - for each position, use it as the "center" and check if there's a palindrome by incrementing r and decrementing l
    - if length of new palindrome > length of prev palindrome, set it as new palindrome
    - two cases: odd and even
        - odd: l = r
        - even: l, r = l + 1

Implement

Review
dfcbbcsf

d
newPalindrome = "d"
f
c
b, cbbc
newPalindrome = "cbbc"
b
c
s
f
return "cbbc"

Evaluate
- Time Complexity: O(n^2) - go through each letter in string, palindrome check could go through entire string in worst case
- Space Complexity: O(n) - returned string could be the entire string in the worst case
"""

def longestPalindrome(s):

    # helper to find a palindrome based on pointers
    # return palindrome string if found
    def findPalindrome(s,l,r):

        # check if l and right are in bounds and palindrome
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        # l+1 because it might go less than 0
        # r since its exclusive
        print(s[l+1:r])
        return s[l+1:r]

    if not s:
        return ""

    finalPalindrome = ""

    # iterate through each letter in the string
    for i in range(len(s)):

        # odd length
        l, r = i, i
        newPalindrome = findPalindrome(s, l, r)
        if len(newPalindrome) > len(finalPalindrome):
            finalPalindrome = newPalindrome

        # even lengths
        l, r = i, i+1
        newPalindrome = findPalindrome(s, l, r)
        if len(newPalindrome) > len(finalPalindrome):
            finalPalindrome = newPalindrome

    return finalPalindrome


print("Expected Output: skshahsks")
print("Actual Output: ", longestPalindrome("skshahsksd"))

print("Expected Output: cbbc")
print("Actual Output: ", longestPalindrome("dfcbbcsf"))




    



