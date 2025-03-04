from typing import *

"""
House Robber
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""
class Solution:
    """
    Recursive Solution would be very expensive: O(2^n)
    Let's use memoization (DP)
    """

    def rob(self, nums: List[int]) -> int:
        # Base case 1) No houses to rob
        if len(nums) <= 0:
            return 0
        
        # Store the max. money you can rob when robbing the prev house or the second prev house
        max_money_prev = nums[0]
        max_money_2prev = 0

        # Calculate solutions starting from the 2nd house
        for i in range(1, len(nums)):
            rob_current_house_money = max_money_2prev + nums[i]

            curr_max_money = max(rob_current_house_money, max_money_prev)

            max_money_2prev = max_money_prev
            max_money_prev = curr_max_money
    

        return max_money_prev

    def rob_simple(self, nums: List[int]) -> int:
        # Base case 1) No houses to rob
        if len(nums) <= 0:
            return 0
        
        # Create a list to store the maximum amount of money for an ever-increasing amount of houses up until len(nums)
        memo_sols = [0] * len(nums)
        
        memo_sols[0] = nums[0]  # The max. money with 1 house is equal to the value of that house

        # Calculate solutions starting from the 2nd house
        for i in range(1, len(nums)):
            max_money_prev = memo_sols[i-1]
            max_money_2prev = memo_sols[i-2] if i >= 2 else 0    # On the 2nd house, there no element 2 houses back, so the money up until then is 0

            rob_current_house_money = max_money_2prev + nums[i]

            memo_sols[i] = max(rob_current_house_money, max_money_prev)
    

        return memo_sols[-1]    # Return the max. amount of money using all the houses



res = Solution()

input1 = [1,1,3,3]
input2 = [2,9,8,3,6]

sol = res.rob(input1)

print("Solution: ", sol)