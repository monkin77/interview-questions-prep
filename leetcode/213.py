from typing import *
import math

'''
House Robber II
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = list([0] * len(nums))
        max_money_wo_first = list([0] * len(nums))

        # Array to store whether the first house will be robbed
        rob_first_house = list([False] * len(nums))

        # Set base cases
        if len(nums) < 2:
            if len(nums) == 0:
                return 0
            return nums[0]
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        rob_first_house[0] = True
        rob_first_house[1] = nums[0] > nums[1]
        max_money_wo_first[0] = 0
        max_money_wo_first[1] = nums[1]
        
        for h_idx in range(2, len(nums)):
            # Recurrency Formulation
            if h_idx == len(nums)-1 and rob_first_house[h_idx-2]:
                # Forced to not rob last house
                max_money[h_idx] = max_money[h_idx-1]
            else:
                max_money[h_idx] = max(nums[h_idx] + max_money[h_idx-2], max_money[h_idx-1])
                # Update rob_first_house array
                if nums[h_idx] + max_money[h_idx-2] > max_money[h_idx-1]:
                    rob_first_house[h_idx] = rob_first_house[h_idx-2]
                else:
                    rob_first_house[h_idx] = rob_first_house[h_idx-1]

            max_money_wo_first[h_idx] = max(nums[h_idx] + max_money_wo_first[h_idx-2], max_money_wo_first[h_idx-1])

        return max(max_money[-1], max_money_wo_first[-1])

    def prev_rob(self, nums: List[int]) -> int:
        max_money = list([0] * len(nums))

        # Array to store whether the first house will be robbed
        rob_first_house = list([False] * len(nums))

        # Set base cases
        if len(nums) < 2:
            if len(nums) == 0:
                return 0
            return nums[0]
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        rob_first_house[0] = True
        rob_first_house[1] = nums[0] > nums[1]
        
        for h_idx in range(2, len(nums)):
            # Recurrency Formulation
            if max_money[h_idx-2]+nums[h_idx] >= max_money[h_idx-1]:
                # Check if it's edge case -> Last House of the Loop
                if h_idx == len(nums)-1 and rob_first_house[h_idx-2]:
                    # If the first house was robbed, we cannot rob the last house
                    # Find the first solution without robbing the first house
                    ignore_first_idx = -1
                    rob_cur_value = nums[h_idx]
                    for i in range(h_idx-2, -1, -1):
                        if not rob_first_house[i]:
                            ignore_first_idx = i
                            break
                    if ignore_first_idx != -1:
                        rob_cur_value += max_money[ignore_first_idx]
                    # Update the max_money for current nº of houses to the between both cases
                    max_money[h_idx] = max(rob_cur_value, max_money[h_idx-1])
                    # NOTE: We don't need to update rob_first_house since this is the last element we are calculating
                else:
                    # Rob the current house
                    max_money[h_idx] = max_money[h_idx-2]+nums[h_idx]
                    rob_first_house[h_idx] = rob_first_house[h_idx-2]
            else:
                # The max. value to rob is the same as the one from the previous house
                max_money[h_idx] = max_money[h_idx-1]
                rob_first_house[h_idx] = rob_first_house[h_idx-1]

        return max_money[-1]

res = Solution()
input1 = [3,4,3]
input2 = [2,9,8,3,6]
input3 = [1,1,1,2]
input4 = [5,1,2,6,12,7,9,3,4,10]

sol = res.rob(input4)

print("Solution: ", sol)