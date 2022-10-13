"""
Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Understand
Check if string palindrome (reads same backwards and forwards) after converting to lowercase and removing all non-alphanumeric characters
"racecar" -> True
" dj kfjsk" -> False
" raceCaR" -> True
"A man, a plan, a canal: Panama" = "amanaplanacanalpanama" -> True

Match
String traversal, left and right pointer

Plan - Iterative Solution
left = pointer on first char, right = pointer on last char
keep iterating until you get to the middle
  for left and right pointer, check if its an alpha num char
      if it isn't, skip it and move to the next char
  check if lowercase char of left and right are equal
      if not, return false
  if they are equal, keep proceeding
return true

Implement

Review
" raceCaR", l = 0, r = 7, skip 0 since it's not alpha num
l = 1, r = 7, r = r
l = 2, r = 6, a = a
l = 3, r = 5, c = c
l = 4, r = 4, while condition stops
return True

Evaluate
Time Complexity: Going through all chars in the string until reach middle, O(n)
Space Complexity: Pointers space don't change, no data structures created, O(1)
"""

def isPalindrome(s):

    # empty case
    if not s:
        return True

    # set pointers
    l, r = 0, len(s) -1

    # iterate while left pointer is less than right
    while l < r:
        # if not alphanumeric, skip
        if not s[l].isalnum():
            l+=1
            continue
        if not s[r].isalnum():
            r-=1
            continue
        # check if lower case values are equal
        if s[l].lower() != s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True

string = "A man, a plan, a canal: Panama"
string2 = " raceCaR"
print("Expected Output: ", True )
print("Actual Output: ", isPalindrome(string))
print("Expected Output: ", True )
print("Actual Output: ", isPalindrome(string2))
