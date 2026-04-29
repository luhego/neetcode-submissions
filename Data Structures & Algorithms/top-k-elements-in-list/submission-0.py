from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        # O(N)
        for num in nums:
            frequencies[num] += 1

        heap = []
        # O(NlogK)
        for num, freq in frequencies.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (freq, num))

        return [h[1] for h in heap]
