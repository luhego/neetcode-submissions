class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, visited):
            if row < 0 or row == n or col < 0 or col == m:
                return

            if (row, col) in visited:
                return

            if grid[row][col] == '0':
                return

            visited.add((row, col))

            dfs(row - 1, col, visited)
            dfs(row + 1, col, visited)
            dfs(row, col - 1, visited)
            dfs(row, col + 1, visited)

        island_count = 0

        n = len(grid)
        m = len(grid[0])
        visited = set()
        for row in range(n):
            for col in range(m):
                if (row, col) in visited or grid[row][col] == '0':
                    continue
                dfs(row, col, visited)
                island_count += 1
        return island_count
