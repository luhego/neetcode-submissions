class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        n = len(grid)
        m = len(grid[0])

        # Find the gates and put them into a queue
        queue = deque([])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
    
        # Multi-source BFS
        while len(queue) > 0:
            row, col, dist = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == n or new_col < 0 or new_col == m:
                    continue

                # Cell is a wall, a gate or it has been visited already. Skip it
                if grid[new_row][new_col] < INF:
                    continue

                grid[new_row][new_col] = dist + 1
                queue.append((new_row, new_col, dist + 1))