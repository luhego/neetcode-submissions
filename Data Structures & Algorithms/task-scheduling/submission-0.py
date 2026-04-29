from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        max_heap = []
        for task, freq in freqs.items():
            heappush(max_heap, (-freq, task))

        queue = deque()
        time = 0
        while len(queue) > 0 or len(max_heap) > 0:
            time += 1

            if len(max_heap) > 0:
                freq, task = heappop(max_heap)
                freq += 1
                if freq != 0:
                    queue.append((freq, task, time + n))

            if len(queue) > 0 and queue[0][2] == time:
                freq, task, _ = queue.popleft()
                heappush(max_heap, (freq, task))

        return time