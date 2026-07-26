"""
Time complexity: O(NlogN)
Space complexity: O(N) from sorting algorithm
Time: 3min
"""
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            prev, current = intervals[i - 1], intervals[i]
            if prev.end > current.start:
                return False
        return True
