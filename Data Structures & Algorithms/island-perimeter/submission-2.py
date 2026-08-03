"""
N: number of rows
M: number of columns
Time complexity: O(N*M)
Space complexity: O(N*M)
Time: 10min

Intuition: every time we go outside of the limits or go to a cell with water we touch an edge.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row == n_rows or col < 0 or col == n_cols:
                return 1

            if grid[row][col] == 0:
                return 1

            if (row, col) in seen:
                return 0

            seen.add((row, col))
            
            perimeter = 0
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
