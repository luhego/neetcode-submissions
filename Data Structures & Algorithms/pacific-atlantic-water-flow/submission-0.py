class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, index):
            while len(queue) > 0:
                r, c = queue.popleft()
                grid[r][c][index] = 1

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + dr, c + dc

                    # Invalid limits
                    if new_r < 0 or new_r == m or new_c < 0 or new_c == n:
                        continue

                    # Cell already visited or height is smaller
                    if grid[new_r][new_c][index] == 1 or heights[new_r][new_c] < heights[r][c]:
                        continue
                    
                    queue.append((new_r, new_c))

        m = len(heights)
        n = len(heights[0])

        grid = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Start bfs from cells adjacent to pacific
        queue = deque([])
        for r in range(m):
            queue.append((r, 0))
        for c in range(n):
            queue.append((0, c))

        bfs(queue, 0)

        # Start bfs from cells adjacent to atlantic
        queue = deque([])
        for r in range(m):
            queue.append((r, n - 1))
        for c in range(n):
            queue.append((m - 1, c))

        bfs(queue, 1)

        result = []
        for r in range(m):
            for c in range(n):
                if sum(grid[r][c]) == 2:
                    result.append([r, c])


        return result
