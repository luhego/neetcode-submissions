class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row == n or col < 0 or col == m:
                return 0
            if (row, col) in visited or grid[row][col] == 0:
                return 0

            visited.add((row, col))
            area = 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

            return area


        n = len(grid)
        m = len(grid[0])

        visited = set()
        max_area = 0
        for row in range(n):
            for col in range(m):
                if (row, col) in visited or grid[row][col] == 0:
                    continue
    
                curr_area = dfs(row, col)
                max_area = max(max_area, curr_area)

        return max_area