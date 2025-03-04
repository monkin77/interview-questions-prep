from typing import *
import math

"""
Maximum Subarray
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0

        max_sum = -math.inf

        curr_sum = 0
        
        for r in range(len(nums)):
            curr_num = nums[r]

            # If the sum of the numbers up until now is > 0: Add the current number
            if curr_sum >= 0:
                curr_sum += curr_num
            # If the sum is negative, ignore the numbers up until now
            elif curr_sum < 0:
                # Set the subarray start to this number
                l = r
                curr_sum = curr_num

            # Update the max sum
            max_sum = max(max_sum, curr_sum)

        
        return max_sum
        

res = Solution()

input1 = [2,-3,4,-2,2,1,-1,4]
input2 = [-1]
input3 = [-2,-1]

sol = res.maxSubArray(input3)

print("Solution: ", sol)