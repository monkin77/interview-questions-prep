from typing import *

"""
Find Minimum in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        if len(nums) <= 1:
            return nums[0]

        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        
        return min(nums[mid], self.findMin(nums[:mid]), self.findMin(nums[mid+1:]))


res = Solution()

input1 = [3,4,5,6,1,2]
input2 = [4,5,0,1,2,3]
input3 = [4,5,6,7]

sol = res.findMin(input1)

print("Solution: ", sol)