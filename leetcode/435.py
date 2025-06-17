from typing import *

'''
Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.
'''
class Solution:
    @staticmethod
    def init_list_of_objects(size) :
        list_of_objects = list()
        for i in range(size):
            list_of_objects.append(list())  # object w/ a different reference
        return list_of_objects
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy approach
        '''
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res


    def old_eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time and desc. end time upon tie
        # Time Complexity: O(n * log n)
        intervals.sort(key=lambda x: (x[0], -x[1])) 

        # List store the nº of collisions of each interval
        num_collisions: list = [0] * len(intervals)
        # List stores the index of colliding intervals. Shape: (num_intervals, num_collisions)
        collisions_per_interval: list[list] = self.init_list_of_objects(len(intervals))

        # Stores the index of the active intervals
        active_intervals: set = set()

        # Store number of intervals that need to be removed
        num_removes = 0

        # Calculate the nº of collisions per interval - Time Complexity: O(n^2)
        for i in range(len(intervals)):
            # (start, end) time of the new interval
            start, end = intervals[i]

            # Check special case: Exactly the same interval
            if i > 0:
                start2, end2 = intervals[i-1]
                if start == start2 and end == end2:
                    # Same interval -> must be removed
                    num_removes += 1
                    continue

            # Remove intervals from active_intervals that became inactive (out of the window)
            # If still active, increment the nº of collisions - Time Complexity: O(n)
            remove_idx: set = set()
            for active_idx in active_intervals:
                _cur_start, cur_end = intervals[active_idx]

                # If the new interval starts at least at the end of the previous interval -> no collision -> remove from active_intervals
                # NOTE: Can I remove during iteration?
                if start >= cur_end:
                    remove_idx.add(active_idx)
                    # active_intervals.remove(active_idx)
                else:
                    # Add collision to the collisions_per_interval list (bi-directional)
                    collisions_per_interval[active_idx].append(i)
                    collisions_per_interval[i].append(active_idx)
            # Remove the elements
            for rem_idx in remove_idx:
                active_intervals.remove(rem_idx)

            # Add new interval to the active_intervals set
            active_intervals.add(i)
            
        # Update the num_collisions list
        num_collisions = [len(cur_collisions) for cur_collisions in collisions_per_interval]

        # While Loop to remove colliding intervals
        while sum(num_collisions) > 0:
            # Remove the next interval w/ most collisions
            # Find index with most collisions
            max_collisions_idx = num_collisions.index(max(num_collisions))

            # Remove the Max Interval from the collisions_per_interval array
            for associated_interval_idx in collisions_per_interval[max_collisions_idx]:
                # Remove the interval with the most collisions from the other intervals' collision lists
                collisions_per_interval[associated_interval_idx].remove(max_collisions_idx)
            collisions_per_interval[max_collisions_idx] = []

            # Update the num_collisions list
            num_collisions = [len(cur_collisions) for cur_collisions in collisions_per_interval]

            # Update num_removes
            num_removes += 1
        
        return num_removes



res = Solution()
input1 = [[1,2],[2,4],[1,4]]
input2 = [[1,2],[2,4]]
input3 = [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]

sol = res.eraseOverlapIntervals(input3)

print("Solution: ", sol)