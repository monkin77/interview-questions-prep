from typing import *
import math

"""
Insert New Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        found_relation = False

        for idx, interval in enumerate(intervals):
            newStart, newEnd = newInterval[0], newInterval[1]
            currStart, currEnd = interval[0], interval[1]

            if newEnd < currStart:
                # If the new interval finishes before the current begins
                # Insert the new interval before the current
                intervals = intervals[:idx] + [newInterval] + intervals[idx:]
                found_relation = True
                break
            if (newStart <= currStart and newEnd >= currStart) or (currStart <= newStart and currEnd >= newStart):
                # If the new interval and the current interval are intersected -> Get the min for the start and max for the end of the interval
                modified_interval = [min(newStart, currStart), max(newEnd, currEnd)]

                # Check if any of the following interval also intersects now
                final_merged_idx = None
                for idx2 in range(idx+1, len(intervals)):
                    nextInterval = intervals[idx2]
                    if nextInterval[0] <= modified_interval[1]:
                        # If the next interval start is <= to the end of the modified interval: add them together
                        modified_interval[1] = max(modified_interval[1], nextInterval[1])
                        final_merged_idx = idx2
                    else:
                        break

                intervals[idx] = modified_interval
                if final_merged_idx != None:
                    # Remove the elements of the array that were merged
                    intervals = intervals[:idx+1] + intervals[final_merged_idx+1:]

                found_relation = True
                break

            # Else: The interval is not related to the current interval

        if not found_relation:
            intervals.append(newInterval)


        return intervals
        

res = Solution()

input1 = [[[1,3],[4,6]], [2,5]]
input2 = [[[1,2],[3,5],[9,10]], [6, 7]]
input3 = [-2,-1]

sol = res.insert(input1[0], input1[1])

print("Solution: ", sol)