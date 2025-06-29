from typing import *
from bisect import bisect_left

"""
Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

"""
class Solution:
    '''
    Binary Search Solution: Use a list to store the smallest end values of subsequences of different lengths.
    For each number, use binary search to find the position in the list where it can replace an existing end value
    or extend the list.

    Time Complexity: O(n * log(n))
    Space Complexity: O(n)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # List to store the smallest end values of subsequences

        # Outer loop time complexity: O(n)
        for num in nums:
            # Find the position to replace or extend using binary search
            # Time Complexity: O(log n)
            pos = bisect_left(sub, num)
            if pos == len(sub):
                # If num is larger than all elements, extend the subsequence
                sub.append(num)
            else:
                # Replace the element at the found position
                sub[pos] = num

        # The length of the list is the length of the LIS
        return len(sub)

    '''
    Heuristic Solution: Only store the minimum nº for each subsequence size and progressively try to increase
    the subsequence from left to right

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    def heuristic_lengthOfLIS(self, nums: List[int]) -> int:
        max_len = 0
        MAX_NUM = 1001

        max_num_per_len = {}    # Map containing the maximum number for each length of increasing subsequence

        for num in nums:
            # Iterate through the lengths in reverse order
            for length in range(max_len, 0, -1):
                if length in max_num_per_len:
                    if num > max_num_per_len[length]:
                        # Can add number to subsequence -> update the maximum number for the current subsequence size.
                        # Make it as small as possible -> accepts more subsequences
                        max_num_per_len[length+1] = min(max_num_per_len.get(length+1, MAX_NUM), num) 

                        # Update max_len
                        if length + 1 > max_len:
                            max_len = length+1

            # Special case: Add the number as the first element of the sequence
            # Make it as small as possible -> accepts more subsequences
            max_num_per_len[1] = min(max_num_per_len.get(1, MAX_NUM), num)
            # Update max_len
            if max_len < 1:
                max_len = 1
                        
            
        return max_len

    
    '''
    Naive Solution
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    '''
    def lengthOfLIS_naive(self, nums: List[int]) -> int:
        max_len = 0

        visited_subseqs = set()

        for i in range(len(nums)):
            num = nums[i]

            new_elems: set = set()
            for subseq in visited_subseqs:
                # If current number can be added to the subsequence
                if subseq[-1] < num:
                    # Create a new tuple for the new subsequence
                    new_subseq = subseq + (num,)

                    if len(new_subseq) > max_len:
                        max_len = len(new_subseq)

                    # Add new subseq
                    new_elems.add(new_subseq)
            # Add all new subsequences to the visited set
            visited_subseqs.update(new_elems)


            # Also add solution containing only the current number
            if num not in visited_subseqs:
                visited_subseqs.add((num,)) # Convert to tuple for immutability and hashability

                if max_len < 1:
                    max_len = 1
            
        return max_len

res = Solution()

input1 = [9,1,4,2,3,3,7]
input2 = [0,3,1,3,2,3]

sol = res.lengthOfLIS(input1)

print("Solution: ", sol)