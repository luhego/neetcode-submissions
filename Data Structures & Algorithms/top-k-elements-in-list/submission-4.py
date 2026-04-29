import heapq

"""
Time complexity: O(NlogK)
Space complexity: O(N + K)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        min_heap = []
        for num, freq in freqs.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                 if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, num))

        return [val for _, val in min_heap]    