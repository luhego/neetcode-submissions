"""
N: number of cells in the grid
Time complexity: O(N)
Space complexity: O(N)
Time: 5min
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or row == n_rows or col < 0 or col == n_cols:
                return
            if grid[row][col] == "0":
                return
            if (row, col) in seen:
                return

            seen.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)


        n_rows = len(grid)
        n_cols = len(grid[0])

        num_islands = 0
        seen = set()
        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) in seen or grid[row][col] == "0":
                    continue

                dfs(row, col)
                num_islands += 1
        
        return num_islands
        