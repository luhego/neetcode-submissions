"""
Time complexity: O(MN)
Space complexity: O(1)
Time: 12min
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        any_zero_in_row = any(matrix[0][c] == 0 for c in range(n))
        any_zero_in_col = any(matrix[r][0] == 0 for r in range(m))

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if any_zero_in_row:
            for c in range(n):
                matrix[0][c] = 0
        
        if any_zero_in_col:
            for r in range(m):
                matrix[r][0] = 0