"""
Time complexity: O(NlogN)
Space complexity: O(N)
Time: 17min
"""
from heapq import heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = defaultdict(int)
        for task in tasks:
            task_freqs[task] += 1

        max_heap = []
        for task, freq in task_freqs.items():
            heappush(max_heap, (-freq, task))
        
        queue = deque([])

        t = 0
        while max_heap or queue:
            # Add elegible tasks back into the heap
            while queue and queue[0][0] == t:
                _, task, freq = queue.popleft()
                heappush(max_heap, (-freq, task))

            # Run one cycle
            t += 1

            if max_heap:
                freq, task = heappop(max_heap)
                freq *= -1

                if freq > 1:
                    freq -= 1
                    queue.append((t + n, task, freq))
                
        
        return t

