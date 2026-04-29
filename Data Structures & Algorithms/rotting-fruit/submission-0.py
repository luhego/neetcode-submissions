class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        queue = deque([])
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        max_time = 0
        while len(queue) > 0:
            row, col, t = queue.popleft()
            max_time = max(max_time, t)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == nrows or new_col < 0 or new_col == ncols:
                    continue

                if grid[new_row][new_col] in [0, 2]:
                    continue

                grid[new_row][new_col] = 2
                queue.append((new_row, new_col, t + 1))


        return -1 if any(1 in row for row in grid) else max_time
