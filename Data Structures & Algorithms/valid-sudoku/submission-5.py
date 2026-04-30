"""
Time complexity: O(N^2). For this example: O(81) ~ O(1)
Space complexity: O(N^2). For this instance: O(81) ~ O(1)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if val == ".":
                    # not a number, continue
                    continue
                box_index = 3 * (row // 3) + col // 3
                if val in row_sets[row] or val in col_sets[col] or val in boxes[box_index]:
                    return False
                row_sets[row].add(val)
                col_sets[col].add(val)
                boxes[box_index].add(val)

        return True                
