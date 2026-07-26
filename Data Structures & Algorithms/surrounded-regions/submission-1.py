
"""
Time complexity: O(MN)
Space complexity: O(1)
Time: 17min
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            if (row, col) in seen:
                return True

            if row < 0 or row == m or col < 0 or col == n:
                return True

            if board[row][col] == "X":
                return True

            seen.add((row, col))

            # region is not surrounded
            is_surrounded = not (row == 0 or row == m - 1 or col == 0 or col == n - 1)

            b1 = dfs(row - 1, col)
            b2 = dfs(row + 1, col)
            b3 = dfs(row, col - 1)
            b4 = dfs(row, col + 1)

            return is_surrounded and b1 and b2 and b3 and b4

        def capture(row, col):
            board[row][col] = "X"
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
                    continue
                if board[new_row][new_col] == "X":
                    continue
                
                capture(new_row, new_col)

        m, n = len(board), len(board[0])

        seen = set()
        for row in range(m):
            for col in range(n):
                if board[row][col] == "X":
                    continue

                if (row, col) in seen:
                    continue

                is_surrounded = dfs(row, col)

                if is_surrounded:
                    capture(row, col)