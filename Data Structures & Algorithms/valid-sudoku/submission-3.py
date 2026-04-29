class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        box_sets = [set() for _ in range(n)]

        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if val == ".":
                    continue
        
                box_index = 3 * (row // 3) + (col // 3)
                if val in row_sets[row] or val in col_sets[col] or val in box_sets[box_index]:
                    return False

                row_sets[row].add(val)
                col_sets[col].add(val)
                box_sets[box_index].add(val)

        return True