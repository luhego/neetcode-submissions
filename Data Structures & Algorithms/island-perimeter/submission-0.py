class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(row, col, visited):
            if (row, col) in visited:
                return 0
    
            visited.add((row, col))

            perimeter = 4
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == n or new_col < 0 or new_col == m or grid[new_row][new_col] == 0:
                    continue
                else:
                    # Decrease the perimeter by 1 for each valid neighbor
                    perimeter -= 1

                perimeter += dfs(new_row, new_col, visited)

            return perimeter

        perimeter = 0
        visited = set()

        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            for col in range(m):
                if (row, col) in visited or grid[row][col] == 0:
                    continue
                
                perimeter = dfs(row, col, visited)

        return perimeter
        