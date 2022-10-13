"""
Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Understand
- palindrome: word/phrase thats the same going forward and backward
- return length of longest palindrome that can be built with letters in a string
- only contains lowercase or uppercase letters
- case sensitive 
    - 'A' not same as 'a'
- 'aAaa' != palindrome
- there can be one unique letter in the middle

Match
- String

Plan
- if length of s == 1, return 1
- create length variable that we will return
- create dict to store the occurrences of each lowercase and uppercase letter
- iterate through all frequencies
    - if its even, add it to the length variable
    - if its odd and greater than 1, subtract 1 and add it to the length variable
- if output < len(s), that means theres a remainder and we can just add 1 to account for the middle char


Implement

Review
s = "abccccdd"
- counter = { a: 1, b: 1, c: 4, d: 2}
- length = 3 + 2 = 6
- length < len(s), length + 1 = 7
- return 7

Evaluate
- Time Complexity: O(n) - constructing counter, iterating through values
- Space Complexity: O(n) - create dict

"""

from collections import Counter

def longestPalindrome(s):

    if len(s) == 1:
        return 1

    length = 0

    # creates dict with char as keys and frequencies as values
    counter = Counter(s)

    for val in counter.values():
        # if even, add to length
        if val % 2 == 0:
            length += val
        # if odd and greater than 1, decrement val and add to length
        if val % 2 == 1 and val > 1:
            length += val - 1
    # if length less than length of string, there's a remainder. can add 1 to account for middle char
    if length < len(s):
        length +=1
    return length


print("Expected Output: 7")
print("Actual Output:", longestPalindrome("abccccdd"))
