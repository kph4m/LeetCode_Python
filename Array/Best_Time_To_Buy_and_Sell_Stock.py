"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Understand
[5,3,2,6] -> 6-2 = 4
[] = 0
[7,5] = 0

Match
Array traversal, left and right pointer, calculate profit for each combination and store it, if no negative values, return the max

Plan
Initial Plan: Time limit exceeded
create left, right pointer
compare left (i) and right (i+1) pointer, if left > right, calculate profit and store in variable, increase index of right pointer by 1
when right pointer goes through all the elements, increment left and go through all the other elements using right
return maxp

Optimal Plan
create left, right pointer
create maxp variable
while r is less than len(prices)
  if prices[left] < prices [right]
     profit = right - left
     if profit > maxp, profit = maxp
  else change left pointer to right (found a value smaller than the current left)
  increase right pointer by 1

Implement

Review
Intial Plan
l = 0, r = 1, maxp = 3, while stop condition = l index = 2
l = 0, r = 2, maxp = 3, 
l = 0, r = 3, maxp = 3, reset r and increment l
l = 1, r = 2, maxp = 3
l = 1, r = 3, maxp = 3, reset r and increment l
l = 2, r = 3, maxp = 3, reset r and increment l
l = 3, stop while loop
profits not empty, return max(profits) = 3

optimized plan
[3,6,10,5,11,2,12]
l = 0, r = 1, maxp = 3
l = 0, r = 2, maxp = 7
l = 0, r = 3, maxp = 7
l = 0, r = 4, maxp = 8
l = 0, r = 5
l = 5, r = 6, maxp = 9
return 9

Evaluate
Initial Plan
Time Complexity: Go through each input and calculate profit for each subsequent element, right doesn't go through entire input again, therefore O(nlogn)
Space Complexity: Possible profits decrease with each increment of l, therefore O(nlogn)

Optimized Plan
Time Complexity: Go through all elements once, O(n)
Space Complexity: Just used maxp variable, O(1)

# Naive Solution
def maxProfit(prices):

    left,right = 0,1

    maxP = 0

    while left < len(prices) - 1:
        # if left > right, add to profits 
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            if profit > maxP:
                maxP = profit
        # increment left when right reaches the end
        if right == len(prices) - 1:
            left+=1
            right = left+1
            continue
        right+=1
    return maxP
"""

def maxProfit(prices):
    left, right = 0,1
    maxp = 0

    while right < len(prices):
        # check if left less than right
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            # update maxp
            if profit > maxp:
                maxp = profit
        # change left to right because we found an int less than current left
        else:
            left = right
        right+=1
    
    return maxp

prices = [3,6,2,1]
prices2 = [7,4,3,2]
prices3 = [7,1,5,3,6,4]

if __name__ == "__main__":
    print("Expected Output: 3")
    print("Actual Output", maxProfit(prices))

    print("Expected Output: 0")
    print("Actual Output", maxProfit(prices2))

    print("Expected Output: 5")
    print("Actual Output", maxProfit(prices3))
