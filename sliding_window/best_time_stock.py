# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Example 3:
# Input: prices = [2,1,4,5,6]
# Output: 5
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# Thoughts
# A stock can be bought on any day but only sold the days after. A brute force solution would be to search for every ith position and compare
# every i+n position making it O(n^2). First off, there has to be a tracker on max profit and a
# criteria for moving the pointers either right from the left or left from the right. A simple way to narrow the window would be that
# if right - left < 0, we know that left is larger, so the left pointer would increase. If not, the pointer can slide from right to left.
# This wouldn't solve for example 3. The next thing you can do is to create two lists, highest and lowest up to that index, and then
# find out the max by high - low for each point. This would loop through the prices twice and once for comparing, so O(n) time and O(n) space.
# The algorithm could technically run in two passes, the second pass can also do the calculations

def best_time_stock(prices: list[int]):
    list_length = len(prices)
    lows = [0] * list_length
    highs = [0] * list_length
    lowest = prices[0]
    highest = prices[-1]
    max_profit = 0

    for i in range(0, list_length):
        lowest = min(prices[i], lowest)
        lows[i] = lowest

    for i in range(list_length-1, 0, -1):
        highest = max(prices[i], highest)
        highs[i] = highest

    for i in range(0, list_length):
        max_profit = max(highs[i] - lows[i], max_profit)

    return max_profit

print(best_time_stock([7,1,5,3,6,4]))
print(best_time_stock([7,6,4,3,1]))
print(best_time_stock([2,1,4,5,6]))
print(best_time_stock([1,2]))
