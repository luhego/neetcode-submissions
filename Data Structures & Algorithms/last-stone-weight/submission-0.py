from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heappush(max_heap, -stone)

        while len(max_heap) > 1:
            y = -heappop(max_heap)
            x = -heappop(max_heap)

            if y > x:
                heappush(max_heap, -(y - x))
        
        return -max_heap[0] if len(max_heap) > 0 else 0