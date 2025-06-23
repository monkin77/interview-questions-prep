from typing import *

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]

(start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        '''
        if len(intervals) < 2:
            return True
        
        # Sort the meeting times by start time
        intervals.sort(key=lambda x: (x.start, x.end))

        # Iterate meetings
        prev_end = intervals[0].end
        for new_interval in intervals[1:]:
            if new_interval.start < prev_end:
                # Meetings collide
                return False
                
            # Update prev end
            prev_end = new_interval.end
        
        return True



res = Solution()

input1 = [Interval(0, 30), Interval(5,10),Interval(15,20)]
input2 = [Interval(5,8),Interval(9,15)]

sol = res.canAttendMeetings(input2)

print("Solution: ", sol)