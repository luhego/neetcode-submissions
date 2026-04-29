from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda p1: (p1[0] ** 2 + p1[1] ** 2) ** 0.5

        max_heap = []
        for point in  points:
            dist = distance(point)
            if len(max_heap) < k:
                heappush(max_heap, (-dist, point))
            elif dist < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-dist, point))
    
        return [p for _, p in max_heap]