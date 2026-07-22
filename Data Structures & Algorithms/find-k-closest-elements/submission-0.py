from heapq import heappush, heappop

"""
Time complexity: O(Nlogk + klogk)
Space complexity: O(N)
Time: 7min
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for num in arr:
            if len(min_heap) < k:
                heappush(min_heap, (-abs(num - x), num))
            elif -min_heap[0][0] > abs(num - x):
                heappop(min_heap)
                heappush(min_heap, (-abs(num - x), num))
        
        return sorted([entry[1] for entry in min_heap])