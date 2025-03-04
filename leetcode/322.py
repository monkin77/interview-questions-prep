from typing import *
import math

"""
Coin Change
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # List storing the fewest number of coins to make the change for each target amount up until the max amount
        coins_dp = [{} for _ in range(amount+1)]

        # Make sure the coins list is sorted
        coins.sort()

        # Base case 1) For target amount 0, we need 0 coins of each
        coins_dp[0] = {coin: 0 for coin in coins}
        coins_dp[0]['num_coins'] = 0    # Add a key with the number of coins

        for target in range(1, amount+1, 1):
            # IF the target is > the smallest coin, it's not possible to retrieve it
            if target < coins[0]:
                # Mark solution as impossible
                coins_dp[target] = {'num_coins': -1}
                continue

            possible_coins = filter(lambda coin: coin <= target, coins)
            min_coins_used = math.inf
            min_coins_map = {}

            for curr_coin in possible_coins:
                remaining_target = target - curr_coin
                if coins_dp[remaining_target]["num_coins"] < 0:
                    # Impossible solution
                    continue

                if 1 + coins_dp[remaining_target]["num_coins"] < min_coins_used:
                    min_coins_used = 1 + coins_dp[remaining_target]["num_coins"]

                    min_coins_map = coins_dp[remaining_target].copy()
                    # Update the map with the new coin
                    min_coins_map[curr_coin] += 1
                    min_coins_map['num_coins'] += 1
            
            if min_coins_map == {}:
                # No solution found
                min_coins_map = {'num_coins': -1}
            
            coins_dp[target] = min_coins_map

        print(coins_dp)
        num_coins = coins_dp[-1]['num_coins']

        return num_coins
       


res = Solution()

input1 = ([1,5,10], 12)
input2 = ([2], 3)
input3 = ([1], 0)

sol = res.coinChange(input1[0], input1[1])

print("Solution: ", sol)