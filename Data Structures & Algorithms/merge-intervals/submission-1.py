"""
Time complexity: O(NlogN)
Time: 7min
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        answer = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # Check if overlap
            if end >= interval[0]:
                end = max(end, interval[1])
            else:
                answer.append([start, end])
                start, end = interval

        answer.append([start, end])

        return answer
