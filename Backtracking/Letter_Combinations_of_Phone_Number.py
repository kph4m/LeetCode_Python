"""
Letter Combinations of Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Understand
- given string with digits 2-9, return possible letter combinations
- "34" -> ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]
- duplicates are possible, just do the process normally

Match 
- backtrack

Plan
- create mapping
- create output array
- backtracking algorithm
    - exit condition: if current idx >= len(digits), append to output and return
    - iterate through each char in digit
        - append it to the temp res
        - call backtracking to move on to the next char
        - pop the value from temp tes

              []
        /      \       \
        ['a']   ['b'] ['c']
['ad'] ['ae'] ['af'] ['bd'] ['be'] ['bf'] ['cd'] ['ce'] ['cf']

Implement

Review
'23'

a:
['a','d'], ['a','e'], ['a','f']

b:
['b','d'], ['b','e'], ['b','f']

c:
['c','d'], ['c','e'], ['c','f']


Evaluate
- Time Complexity: O(4**n), 4 choices for each input in the worst case (7777)
- Space Complexity: O(n) - store the result, O(4**n)- recursive stack space: 
"""

def letterCombinations(digits):
    def backtracking(digits, cur_idx, cur_res):

        # exit condition
        if cur_idx >= len(digits):
            res.append("".join(cur_res))
            return
        
        # else iterate through all chars for a digit
        for char in mapping[digits[cur_idx]]:
            cur_res.append(char)
            backtracking(digits, cur_idx+1, cur_res)
            cur_res.pop()

    if not digits:
        return []

    mapping = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi',
        '5': 'jkl', 
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    res = []

    backtracking(digits, 0, [])
    return res


print("Expected Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']")    
print("Actual Output: ", letterCombinations('23'))

print("Expected Output: ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']")    
print("Actual Output: ", letterCombinations('34'))