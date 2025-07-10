from typing import *

"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_intervals: dict[int, list[int]] = {}

        max_consec_len = 0
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        for num in nums:
            if num in num_intervals:
                # Repeated num
                continue

            l, r = num, num
            if (num-1 in num_intervals) and (num+1 in num_intervals):
                # Found Bridge Element (connects 2 intervals)
                min_l, max_l = num_intervals[num-1]
                min_r, max_r = num_intervals[num+1]

                # Update the interval range in both edges
                num_intervals[min_l][1] = max_r # Update max elem. of left interval
                num_intervals[max_r][0] = min_l # Update min elem. of right interval

                # Add interval range for current elem (To register this elem. as visited)
                num_intervals[num] = [min_l, max_r]

                # Define l and r to update max_consec_len
                l, r = min_l, max_r
            elif num-1 in num_intervals:
                # Current num is consecutive to the right
                # Increase interval to the right
                # Find left boundary of the interval
                left_bound = num_intervals[num-1][0]

                # Add Current interval to the dictionary of intervals
                num_intervals[num] = [left_bound, num]
                # Update interval of left boundary
                num_intervals[left_bound][1] = num

                # Define l and r to update max_consec_len
                l, r = left_bound, num
            elif num+1 in num_intervals:
                # Current num is consecutive to the left
                # Increase interval to the left
                # Find right boundary of the interval
                right_bound = num_intervals[num+1][1]

                # Add Current Interval to the dict of intervals
                num_intervals[num] = [num, right_bound]
                # Update interval of right_boundary
                num_intervals[right_bound][0] = num

                # Define l and r to update max_consec_len
                l, r = num, right_bound
            else:
                # Current number is not consecutive to any other number
                # Create new interval
                num_intervals[num] = [num, num]

            # Check if max_consec_len increased
            cur_len = r-l+1
            max_consec_len = max(max_consec_len, cur_len)

        return max_consec_len
        
res = Solution()

input1 = [2,20,4,10,3,4,5]
input2 = [0,3,2,5,4,6,1,1]

sol = res.longestConsecutive(input2)

print("Solution: ", sol)