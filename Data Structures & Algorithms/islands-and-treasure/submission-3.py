"""
Time complexity: O(MN)
Space complexity: O(MN)
Time: 16min
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1

        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                # Outside limits
                if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
                    continue

                # Water cell can't be traversed
                if grid[new_row][new_col] != INF:
                    continue

                grid[new_row][new_col] = grid[row][col] + 1
                queue.append((new_row, new_col))
