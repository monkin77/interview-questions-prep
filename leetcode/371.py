from typing import *
import math

"""
Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the + and - operators.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1  # Calculate the current Carry
            a = (a ^ b) & mask  # Calculate the current Bit value (a = a XOR Previous Carry)
            b = tmp & mask      # Update B to be the carry for the next iteration

        if a > mask // 2:   # Turn negative numbers into positive since Python does not do it automatically
            return ~(a ^ mask)
        else:
            return a
    

res = Solution()

input1 = (1, 1)
input2 = (4, 7)
input3 = (10, 11)
input4 = (20, 30)
input5 = (-1, 1)

sol = res.getSum(input2[0], input2[1])

print("Solution: ", sol)