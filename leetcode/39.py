from typing import *
import math
from collections import deque
import heapq

"""
Combination Target Sum
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Base case 1)
        if target == 0:
            # Reached a solution
            return [[]]
        
        if len(nums) == 0:
            # If target is not 0 and len(nums) is 0
            return None # didn't find a solution using this path
        
        searchingSol = False    # Tracks if there is at least 1 possible solution using this path
        combinations: List[List[int]] = []
        for idx, num in enumerate(nums):
            if num <= target:
                # Search for solutions using this number
                searchingSol = True

                maxFreq = target // num # How many times num can be used

                for freq in range(1, maxFreq+1, 1):
                    numList = [num for _ in range(freq)]

                    # Get the combinations that reach the remaining for target
                    remainSols = self.combinationSum(nums[idx+1:], target-num*freq)

                    if remainSols is None:
                        # No solution down this path
                        continue

                    # Else: If there are solutions
                    for sol in remainSols:
                        # Add solution to the combinations list
                        newSol = numList + sol
                        combinations.append(newSol)
                    
        if not searchingSol:
            # If no number in nums could be used -> Wrong Path
            return None        
        
        return combinations



res = Solution()

input1 = ([2,5,6,9], 9)
input2 = ([3,4,5], 16)

sol = res.combinationSum(input1[0], input1[1])

print("Solution: ", sol)