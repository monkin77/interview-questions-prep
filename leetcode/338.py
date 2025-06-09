from typing import *
import math

'''
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBitsNum(self, num: int, memo_ans: dict[int, int]) -> int:
        '''
        Returns the number of 1s in the bit-representation of number n
        '''
        counter = 0
        while num > 0:
            # Check if num is in the memoization dictionary
            if num in memo_ans:
                print(f"Memoized result found for {num}: {memo_ans[num]}")
                counter += memo_ans[num]
                return counter

            print(num)
            has_one = int((num % 2) != 0)
            counter += has_one
            num >>= 1
        return counter

    '''
    Time Complexity: O(n * log n)
    Space Complexity: O(n)
    '''
    def countBits(self, n: int) -> List[int]:
        num_bits_arr = []
        memo_ans = {}

        for i in range(n+1):
            cur_num_ones = self.countBitsNum(i, memo_ans)
            if i not in memo_ans:
                # Store the result in memoization dictionary
                memo_ans[i] = cur_num_ones

            num_bits_arr.append(cur_num_ones)

        return num_bits_arr

res = Solution()
input1 = 4
input2 = 1
input3 = 0

sol = res.countBits(input1)

print("Solution: ", sol)