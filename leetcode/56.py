from typing import *
import math

'''
Merge Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.
'''
class Solution:
    '''
    Overall Time Complexity: O(n log n)
    Space Complexity: O(n) for storing merged intervals
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the start time
        # Time Complexity: O(n log n) -- sorting
        intervals.sort(key=lambda x: x[0])

        # Create array for merged intervals
        merged_intervals = []

        cur_start, cur_end = intervals[0]
        for i in range(1, len(intervals)):
            new_interval = intervals[i]

            if new_interval[0] <= cur_end:
                # If the start time of the new interval <= end time from previous -> merge
                cur_end = max(cur_end, new_interval[1])
                continue

            # If new interval cannot be merged -> Add interval to merged_intervals
            merged_intervals.append([cur_start, cur_end])
            
            # Update the start and end of the current merged interval
            cur_start, cur_end = new_interval
        
        # Add the last interval to the list of merged_intervals
        merged_intervals.append([cur_start, cur_end])

        return merged_intervals
    
res = Solution()
input1 = [[1,3],[1,5],[6,7]]
input2 = [[1,2],[2,3]]
input3 = 0

sol = res.merge(input2)

print("Solution: ", sol)

