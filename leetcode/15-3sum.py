from typing import *

"""
Three Integer Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []

        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                # If the number is the same
                continue

            twoSumList = nums[idx+1:]
            twoSumSols = self.twoSum(twoSumList, -num)  # Target is -num to sum to 0

            for currSol in twoSumSols:
                sols.append([num] + currSol)
            
        return sols

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        l, r = 0, len(nums) - 1

        sols = []

        prevL = None
        prevR = None
        while l < r:
            if nums[l] == prevL:
                # Ignore duplicate solution
                l += 1
                continue
            if nums[r] == prevR:
                r -= 1
                continue

            currSum = nums[l] + nums[r]
            if currSum == target:
                sols.append([nums[l], nums[r]])

                # Shift the left pointer to the right
                prevL = nums[l]
                l += 1
            elif currSum < target:
                prevL = nums[l]
                l += 1
            else:
                # currSum > target
                prevR = nums[r]
                r -= 1
        
        return sols



res = Solution()

input1 = [0, 1, -1]
input2 = [0,0,0,0]
sol = res.threeSum(input2)
print("Solution: ", sol)