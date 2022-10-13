"""
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Understand
- given an array of coins and the amount, return the lowest number of coins that can be used to sum up the amount
- if no possible coin combination can sum up to it, return -1
- [1,5,2], 12 -> 3 (5 + 5 + 2) 
- [4,2,6], 15 -> -1 

Match
- Greedy
    - Greedy won't work for all cases
    - [1,3,4,5], 7 -> 3 (1 + 1 + 5) != optimal 
- Dynamic Programming
    - Bottom-Up Approach
        - calculate the coins required to get 0-(amount-1) using the given coins
        - DP[0] = 0
        - DP[1] = 1
        - DP[2] = 1 + DP[1] = 2
        - DP[3] = 1
        - DP[4] = 1
        - DP[5] = 1
        - DP[6] = 1 + DP[1] = 2

        Next, go through each coin in the array and calculate the number of coins needed for the amount
        - DP[7] = DP[1] + DP[6] = 3
        - DP[7] = DP[3] + DP[4] = 2
        - DP[7] = DP[4] + DP[3] = 2
        - DP[7] = DP[6] + DP[1] = 3

Plan
- create list with 0-amount with default values of inf
- indices = coins, values = coins
- iterate through 1...amount
    - iterate through values in coins
        - if difference between value in list and value in coin, is positive
            - update value in list to min(prev value, 1 + dp[difference])
- return dp[amount] if its not the default value
    - if its the default, then no possible combination exists with the coins, return -1


Implement

Review
[1,3,4,5], amount = 7

dp = [0,8,8,8,8,8,8,8]

1 - 1 >= 0
dp[1] = min(8,1) = 1
dp = [0,1,8,8,8,8,8,8]

2 - 1 >=0
dp[2] = min(8, 2) = 2
dp = [0,1,2,8,8,8,8,8]

3 - 1 >=0
dp[3] = min(8, 3) = 3
dp = [0,1,2,3,8,8,8,8]

3-3 >= 0
dp[3] = min(3,1) = 1
dp = [0,1,2,1,8,8,8,8]

4-1 >= 0
dp[4] = min(8,2) = 2
dp = [0,1,2,1,2,8,8,8]

4-3 >= 0
dp[4] = min(2, 2) = 2
dp = [0,1,2,1,2,8,8,8]

4-4 >= 0
dp[4] = min(2,1) = 1
dp = [0,1,2,1,1,8,8,8]

5-1 >= 0
dp[5] = min(8,2) = 2
dp = [0,1,2,1,1,2,8,8]

5-3 >= 0
dp[5] = min(2,3) = 2
dp = [0,1,2,1,1,2,8,8]


5-4 >= 0
dp[5] = min(2,2) = 2
dp = [0,1,2,1,1,2,8,8]

5-5 >= 0
dp[5] = min(2,1) = 1
dp = [0,1,2,1,1,1,8,8]


6-1 >= 0
dp[6] = min(8,2) = 2
dp = [0,1,2,1,1,1,2,8]

6-3 >= 0
dp[6] = min(2,2) = 2
dp = [0,1,2,1,1,2,2,8]

6-4 >= 0
dp[6] = min(2,3) = 2
dp = [0,1,2,1,1,2,2,8]

6-5 >= 0
dp[6] = min(2,2) = 2
dp = [0,1,2,1,1,1,2,8]


7-1 >= 0
dp[7] = min(8,3) = 3
dp = [0,1,2,1,1,1,2,3]

7-3 >= 0
dp[7] = min(3,2) = 2
dp = [0,1,2,1,1,1,1,2]

7-4 >= 0
dp[7] = min(2,2) = 2
dp = [0,1,2,1,1,1,1,2]

7-5 >= 0
dp[7] = min(2,3) = 2
dp = [0,1,2,1,1,1,1,2]

return 2


Evaluate
- Time Complexity: O(n*c), where n is size(0...amount) and c is the total coins
- Space Complexity: O(n)
"""

import math

def coinChange(coins, amount):

    # 0....amount with "infinite" value
    dp = [amount+1] * (amount + 1)

    # 0 takes 0 coins
    dp[0] = 0

    for a in range(1, amount+1):
        for coin in coins:
            # if the difference is non-negative
            if a - coin >= 0:
                # recurrence relation
                dp[a] = min(dp[a], 1 + dp[a-coin])

    if dp[amount] != amount+1:
        return dp[amount]
    else:
        return -1 