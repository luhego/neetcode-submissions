from heapq import heappush, heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Time complexity: O(NlogN)
Space complexity: O(N)
Time: 8min
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        min_rooms = 0
        heap = []
        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heappop(heap)
            heappush(heap, interval.end)
            
            min_rooms = max(min_rooms, len(heap))

        return min_rooms