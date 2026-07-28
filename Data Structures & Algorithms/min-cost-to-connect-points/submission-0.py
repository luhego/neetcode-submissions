"""
Time complexity: O(ElogV)
Space complexity: O(V)
Time: 20min
"""
from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build the graph
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                pi = points[i]
                pj = points[j]
                graph[i].append((j, abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])))

        cost = 0
        i = 0
        visited = set([i])
        min_heap = []
        for neighbor in graph[i]:
            heappush(min_heap, (neighbor[1], neighbor[0]))

        while len(visited) < n:
            while min_heap and min_heap[0][1] in visited:
                heappop(min_heap)
            
            dist, j = heappop(min_heap)
            cost += dist
            visited.add(j)
            for k, dist in graph[j]:
                if k in visited:
                    continue
                heappush(min_heap, (dist, k))
        
        return cost

            