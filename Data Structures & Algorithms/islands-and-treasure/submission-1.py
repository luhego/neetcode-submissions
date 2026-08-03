class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2^31 - 1

        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        visited = set()
        while queue:
            row, col, dist = queue.popleft()

            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                # Outside limits
                if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
                    continue

                # Water cell can't be traversed
                if grid[new_row][new_col] == -1:
                    continue

                grid[new_row][new_col] = min(grid[new_row][new_col], dist + 1)
                queue.append((new_row, new_col, dist + 1))
