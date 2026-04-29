class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        si = 0
        ei = 1
        merged_intervals = []

        intervals.sort(key=lambda i: i[0])

        start = intervals[0][si]
        end = intervals[0][ei]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            # intervals overlap
            if curr_interval[si] <= end:
                start = min(start, curr_interval[si])
                end = max(end, curr_interval[ei])
            else:
                merged_intervals.append([start, end])
                start = curr_interval[si]
                end = curr_interval[ei]

        merged_intervals.append([start, end])

        return merged_intervals