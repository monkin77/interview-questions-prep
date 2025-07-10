from typing import *
import bisect

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""
Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.
"""
class Solution:
    '''
    n <- Nº intervals

    Overall Time Complexity: O(n log n)
    Space Complexity: O(n)
    '''
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        # Sort the intervals by asc. start time and asc. end Time in case of Draw
        # Time Complexity: O(n log n)
        intervals.sort(key=lambda interval: (interval.start, interval.end))

        num_days = 0    # Define counter of num_days

        # Space Complexity: O(n)
        booked_meetings: set[int] = set()    # Store index of the meetings already booked
        
        # Time Complexity: O(n) -- upper bound in case all intervals collide
        while len(booked_meetings) < len(intervals):
            # Increment number of days
            num_days += 1

            # Go through the remaining intervals and add valid intervals to the current day
            prev_meeting_end = 0
            next_idx = 0    # Initialize to index of the first meeting we can add to this day
            # Time Complexity: O(log n)
            while next_idx < len(intervals):
                # Find index of the next booking to add
                # Increment next_idx by 1 if already booked
                if next_idx in booked_meetings:
                    next_idx += 1
                    continue
                
                # Else: Add this meeting to the current day
                cur_meeting = intervals[next_idx]
                booked_meetings.add(next_idx)
                prev_meeting_end = cur_meeting.end

                # Binary Search to find the index of the next booking with start time >= prev_meeting_end
                # If none -> will return len(intervals)?
                # Time Complexity: O(log n)
                next_idx = bisect.bisect_left(intervals, prev_meeting_end, key= 
                    lambda interval: interval.start)
        
        return num_days



res = Solution()

input1 = [Interval(0, 30), Interval(5,10),Interval(15,20)]
input2 = [Interval(5,8),Interval(9,15)]

sol = res.minMeetingRooms(input1)

print("Solution: ", sol)