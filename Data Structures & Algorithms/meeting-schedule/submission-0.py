"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n < 2:
            return True

        start, end = 0, 1
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, n):
            # there is an overlap
            if intervals[i].start < intervals[i-1].end:
                return False

        return True
