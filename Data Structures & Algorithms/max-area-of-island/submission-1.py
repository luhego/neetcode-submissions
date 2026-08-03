"""
M: number of rows
N: number of columns
Time complexity: O(M*N)
Spacec complexity: O(M*N)
Time: 5min
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row == n_rows or col < 0 or col == n_cols:
                return 0

            if grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))

            return (
                1 +
                dfs(row - 1, col) +
                dfs(row + 1, col) +
                dfs(row, col - 1) +
                dfs(row, col + 1)
            )

        n_rows = len(grid)
        n_cols = len(grid[0])

        max_area = 0
        visited = set()
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    continue
                
                if (row, col) in visited:
                    visited.add((row, col))
                
                max_area = max(max_area, dfs(row, col))
        
        return max_area