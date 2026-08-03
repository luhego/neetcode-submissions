"""
Time complexity: O(MN)
Space complexity: O(MN)
Time: 10min
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        queue = deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visited.add((row, col))
        
        time = 0
        while queue:
            row, col, time = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
                    continue

                if (new_row, new_col) in visited or grid[new_row][new_col] != 1:
                    continue
                
                visited.add((new_row, new_col))
                grid[new_row][new_col] = 2
                queue.append((new_row, new_col, time + 1))

        if any(value == 1 for row in grid for value in row):
            return -1
        return time
