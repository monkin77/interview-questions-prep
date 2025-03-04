from typing import *

"""
Find Target in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        if len(nums) == 0:
            return -1

        # The sorted array (ascending order) was rotated, meaning that there is an element at which
        # the ascending property does not remain. So we can split the original array into 2 sorted lists
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        
        # Check if the middle number is on the first or second sub-list
        if nums[mid] >= nums[0]:
            # We are at L1
            if nums[mid] > target:
                l1_sol = self.search(nums[:mid], target)
                l2_sol = self.search(nums[mid+1:], target)

                if l1_sol != -1:
                    return l1_sol
                if l2_sol != -1:
                    return mid + 1 + l2_sol # Add the index of the elements up to mid
            elif nums[mid] < target:
                # Solution is bigger than the middle element
                l2_sol = self.search(nums[mid+1:], target)
                if l2_sol != -1:
                    return mid + 1 + l2_sol
        elif nums[mid] < nums[0]:
            # We are at L2
            if nums[mid] > target:
                # Solution is smaller than the middle element
                l2_sol = self.search(nums[:mid], target)
                return l2_sol
            elif nums[mid] < target:
                # Solution bigger than the middle element
                l1_sol = self.search(nums[:mid], target)
                l2_sol = self.search(nums[mid+1:], target)

                if l1_sol != -1:
                    return l1_sol
                if l2_sol != -1:
                    return mid + 1 + l2_sol # Add the index of the elements up to mid


        return -1 # No solution found on this branch

res = Solution()

input1 = ([3,4,5,6,1,2], 1)
input2 = ([3,5,6,0,1,2], 4)
input3 = ([1, 3], 3)
input4 = ([5,1,3], 3)

sol = res.search(input4[0], input4[1])

print("Solution: ", sol)