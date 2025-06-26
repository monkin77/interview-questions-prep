from typing import *

'''
Missing Number 
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
class Solution:
    '''
    Heuristic solution. We can find the missing number by subtracting the expected sum
    of all values by the actual sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        expected_sum = sum(range(0, len(nums)+1))

        return expected_sum - total_sum

    '''
    Time Complexity: O(n * logn)
    '''
    def missingNumber_sort(self, nums: List[int]) -> int:
        # Sort the numbers
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)

            

res = Solution()
input1 = [1,2,3]
input2 = [0, 2]

sol = res.missingNumber(input1)

print("Solution: ", sol)