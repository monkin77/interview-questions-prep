from typing import *
import math

"""
Buy and Sell Crypto
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        minBuy = 10**5    # Bigger than the limit
        minSell = -1

        for price in prices:
            if price < minBuy:
                minBuy = price
                minSell = -1    # Reset the minSell because there is a new minBuy price

            elif price > minSell:
                minSell = price
                currProfit = minSell - minBuy
                if currProfit > maxProfit:
                    maxProfit = currProfit
    
        return maxProfit


res = Solution()

input1 = [10,1,5,6,7,1]
input2 = [10,8,7,5,2]
input3 = [10000,9999,9998,9997,9996,9995,9994,9993,9992,9991,9990]
sol = res.maxProfit(input3)
print("Solution: ", sol)