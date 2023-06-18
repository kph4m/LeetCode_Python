"""
Shifting Letters

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Understand
- shift letters in string
- shift the first letter of s, x times
- shift the first two letters of s, y times
- shift the first three letters of s, z times
- return the final string after all shifts are applied
- s="abc", shifts=[3,5,9]
    - "abc" -> "dbc" -> "igc" -> "rpl"
- s="aaa", shifts=[1,2,3]
    - "aaa" -> "baa" -> "dca" -> "gfd"

Match

Plan
- keep track of total shifts
- iterate through shifts and shift letters
    - subtract shifts[i] from total shifts
- return result

Implement

Review

Evaluate

"""
# Iterating backwards
# Time Complexity: O(n) - iterate through shifts
# Space Complexity: O(n) - strings are immutable in Python so we have to create a new string each time
# def shiftingLetters(s, shifts):
#     total = 0
#     result = ""
#     for i in range(len(shifts)-1, -1, -1):
#         # this keeps track of the total shifts
#         total += shifts[i]
#         # this converts the letter to a number, adds the total shifts, and converts it back to a letter
#         newLetter = chr((ord(s[i]) + total))
#         # if the new letter is greater than z, subtract 26 to wrap around
#         if ord(newLetter) > ord("z"):
#             newLetter = chr(ord(newLetter) - 26)
#         result = newLetter + result
#     return result

# Iterating forwards
# Time Complexity: O(n) - iterate through shifts
# Space Complexity: O(n) - strings are immutable in Python so we have to create a new string each time
def shiftingLetters(s, shifts):
    total = 0
    result = ""
    # get total shifts
    for i in range(len(shifts)):
        total += shifts[i]
    # iterate through shifts
    for i in range(len(shifts)):
        newLetter = chr((ord(s[i]) + total))
         # if the new letter is greater than z, subtract 26 to wrap around
        if ord(newLetter) > ord("z"):
            newLetter = chr(ord(newLetter) - 26)
        result += newLetter
        total -= shifts[i]
    return result

print("Expected Output: rpl")
print("Actual: ", shiftingLetters("abc", [3,5,9]))

print("Expected Output: gfd")
print("Actual Output: ", shiftingLetters("aaa", [1,2,3]))

print("Expected Output: fec")
print("Actual Output: ", shiftingLetters("zzz", [1,2,3]))