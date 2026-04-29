class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col, region, visited):
            if row < 0 or row == nrows or col < 0 or col == ncols or (row, col) in visited or board[row][col] == "X":
                return True

            is_surrounded = True
            if row == 0 or row == nrows - 1 or col == 0 or col == ncols - 1:
                is_surrounded = False

            region.append((row, col))
            visited.add((row, col))

            r2 = dfs(row - 1, col, region, visited)
            r3 = dfs(row + 1, col, region, visited)
            r4 = dfs(row, col - 1, region, visited)
            r5 = dfs(row, col + 1, region, visited)
    
            return is_surrounded and r2 and r3 and r4 and r5

        nrows = len(board)
        ncols = len(board[0])
        visited = set()
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == "O" and (row, col) not in visited:
                    region = []
                    is_surrounded = dfs(row, col, region, visited)
                    if is_surrounded:
                        for r, c in region:
                            board[r][c] = "X"