"""
N: number of cells in the matrix
Time complexity: O(N)
Space complexity: O(N)
Time: 6min
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):
                val = board[row][col]
                if val == ".":
                    continue

                box_idx = 3 * (row // 3) + col // 3
                if val in rows[row] or val in cols[col] or val in boxes[box_idx]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)
        
        return True
        