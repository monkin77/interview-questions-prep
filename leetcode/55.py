from typing import *

'''
Jump Game 
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        r = prev = len(nums) - 1

        while prev >= 0:
            # Check if jump can be made from prev to r
            cur_jump = nums[prev]
            if cur_jump >= r - prev:
                # Jump is valid -> update r to new right element
                r = prev

            # Check if right element is at the start
            if r == 0:
                # Able to build a path
                return True

            # Update the prev pointer to the previous element in the jump list
            prev -= 1

        # Did not find a valid route -> Return False
        return False

    
    def naiveCanJump(self, nums: List[int]) -> bool:
        '''
        Naive Solution
        Time Complexity: O(n^n)
        '''
        if len(nums) == 1:
            # Reached the last index
            return True
        if len(nums) < 1:
            # Went over the last index
            return False

        max_next_jump = nums[0]

        # Search for a valid solution
        for jump_len in range(1, max_next_jump+1):
            if self.canJump(nums[jump_len:]):
                return True
        
        # If no valid solution -> return False
        return False

res = Solution()
input1 = [1,2,0,1,0]
input2 = [1,2,1,0,1]
input3 = [2,0]

input = input3
sol = res.canJump(input)

print("Solution: ", sol)