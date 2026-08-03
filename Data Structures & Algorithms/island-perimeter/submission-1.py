"""
N: number of rows
M: number of columns
Time complexity: O(N*M)
Space complexity: O(N*M)
Time: 10min
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def calculatePerimeter(row, col):
            perimeter = 4

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == n_rows or new_col < 0 or new_col == n_cols:
                    continue

                if grid[new_row][new_col] == 1:
                    perimeter -= 1

            return perimeter

        def dfs(row, col):
            if row < 0 or row == n_rows or col < 0 or col == n_cols:
                return 0

            if grid[row][col] == 0:
                return 0

            if (row, col) in seen:
                return 0

            seen.add((row, col))
            
            perimeter = calculatePerimeter(row, col)
            perimeter += dfs(row - 1, col)
            perimeter += dfs(row + 1, col) 
            perimeter += dfs(row, col - 1)
            perimeter += dfs(row, col + 1)

            return perimeter

        seen = set()
        n_rows = len(grid)
        n_cols = len(grid[0])
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    continue
                
                return dfs(row, col)
        
        return -1
