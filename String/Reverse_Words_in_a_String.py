"""
Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Understand
- given string, reverse the words chronologically (don't reverse the words themselves, just the order)
- "Hello  my name is" -> "is name my Hello"
- "Hello" -> "Hello"
- "" -> ""

Match
- String

Plan
- use split to create a list of all the words in the string
- reverse the list so they're in reversed chronological order
- use join to add all the words into a string, with spaces in-between each word

Implement

Review
"Hello my name is"
- split: ["Hello", "my", "name", "is"]
- reverse: ["is", "name", "my", "Hello"]
- join: "is name my Hello"

Evaluate
- Time Complexity: O(n) - split, reverse, join
- Space Complexity: O(n) - list of words
"""

def reverseWord(s):

    # split words into list
    s = s.split()

    # reverse the list
    s = s[::-1]

    # add all words in the list to a string with spaces between them
    return " ".join(s)


str = "Hello my name is"
print("Expected Output: 'is name my Hello'")
print("Actual Output: ", reverseWord(str))