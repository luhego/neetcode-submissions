"""
# (i, j) -> (j, n - i - 1)
# Transpose: (i, j) -> (j, i)
# Revese: (j, i) -> (j, n - i - 1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        for row in matrix:
            row.reverse()
