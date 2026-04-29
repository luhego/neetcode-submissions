class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if val == ".":
                    continue

                box_index = 3 * (row // 3) +  col // 3
                if val in rows[row] or val in cols[col] or val in boxes[box_index]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box_index].add(val)
        
        return True
