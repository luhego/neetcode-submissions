from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, val)

        return self.min_heap[0]