"""
M: 9
N: 9
B: 9
Time complexity: O(MN)
Space complexity: O(M + N + B)
Time: 6min
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row_sets = [set() for _ in range(N)]
        col_sets = [set() for _ in range(N)]
        box_sets = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):
                val = board[row][col]
                if val == ".":
                    continue

                box_index = 3 * (row // 3) + col // 3
                if val in row_sets[row] or val in col_sets[col] or val in box_sets[box_index]:
                    return False
                
                row_sets[row].add(val)
                col_sets[col].add(val)
                box_sets[box_index].add(val)
        
        return True