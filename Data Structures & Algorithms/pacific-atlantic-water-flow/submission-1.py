"""
Time complexity: O(MN)
Space complexity: O(MN)
Time: 20min

Approach:

We have two options:
Option 1:
Start bfs from each island and add it to the result array if it reaches both pacific and atlantic

Option 2:
Start bfs from each island that is neighbor to pacific or atlantic, add a marker to indicate whether it can reach either ocean.
Return islands that can reach both.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(q, i):
            while q:
                r, c = q.popleft()
    
                grid[r][c][i] = 1

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr == m or nc < 0 or nc == n:
                        continue


                    if grid[nr][nc][i] == 1 or heights[nr][nc] < heights[r][c]:
                        continue
                    
                    queue.append((nr, nc))

        m, n = len(heights), len(heights[0])
        grid = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Start bfs from pacific
        queue = deque([])
        for c in range(n):
            queue.append((0, c))
        for r in range(m):
            queue.append((r, 0))
        
        bfs(queue, 0)

        # Start bfs from atlantic
        queue = deque([])
        for c in range(n):
            queue.append((m - 1, c))
        for r in range(m):
            queue.append((r, n - 1))
        
        bfs(queue, 1)

        result = []
        for r in range(m):
            for c in range(n):
                if sum(grid[r][c]) == 2:
                    result.append((r, c))
        
        return result
