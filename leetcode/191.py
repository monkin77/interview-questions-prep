from typing import *
import math

"""
Number of One Bits
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        curr_count = 0

        while n > 0:
            curr_count += n & 1 # Add 1 if the current right-wise bit is 1

            n >>= 1     # Shift right 1 -> Divide by 2
            print(n, curr_count)

        return curr_count


res = Solution()

input1 = 0b00000000000000000000000000010111
input2 = 0b01111111111111111111111111111101

sol = res.hammingWeight(input1)

print("Solution: ", sol)