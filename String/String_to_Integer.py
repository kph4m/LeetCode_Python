"""
sing to Integer

Implement the myAtoi(sing s) function, which converts a sing to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(sing s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the sing) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the sing is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the sing after the digits.

Understand
- given sing with ints, return the int representation
- might have white spaces, non-ints
    - just want to return the int value
- can be negative
- "-42" -> -42
- "hello 23" -> 23
- " 123" -> 123


Match
- sing, convert char to int without using int()

Plan
- strip all white spaces
- iterate through all chars in the string
    - account for signage
        - create sign variable
        - if negative, sign = -1
    - make sure they're numbers (0-9) and less than the len of the sing
        - output = output * 10 + convert char to int (using ord)
- return output * sign

Implement

Review
" -123"
- remove white space: "-123"
- - detected, sign = -1
- 1: output = 0 * 10 + ord(1) - ord(0)
    - 0 + (49 - 48)
    - 1
- 2: output = 1 * 10 + ord(2) - ord(0)
    - 10 + (50 - 48)
    - 12
- 3: output = 12*10 + ord(3) - ord(0)
    - 120 + (51 - 48)
    - 123
- 123 * -1
- -123

Evaluate
- Time Complexity: O(n) - iterate through string
- Space Complexity: O(1)

"""
def myAtoi(s):

    if not s:
        return 0

    sign = 1
    output = 0

    # remove white spaces
    s = s.replace(" ", "")

    for i in range(len(s)):
        if s[i] == '-':
            sign = -1
        # convert string int into int and add it to the output
        elif '0' <= s[i] <= '9':
            output = output * 10 + ord(s[i]) - ord('0')
    return sign * output


print("Expected Output: -123")
print("Actual Output: ", myAtoi(" -123"))








