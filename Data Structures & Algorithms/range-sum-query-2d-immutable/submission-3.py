"""
Time complexity: O(MN)
Space complexity: O(MN)
Time: 17min
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.prefix = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                self.prefix[row][col] = matrix[row][col]
                self.prefix[row][col] += self.prefix[row][col - 1] if col > 0 else 0
                self.prefix[row][col] += self.prefix[row - 1][col] if row > 0 else 0
                self.prefix[row][col] -= self.prefix[row - 1][col - 1] if row > 0 and col > 0 else 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix[row2][col2]
        if row1 > 0:
            result -= self.prefix[row1 - 1][col2]
        if col1 > 0:
            result -= self.prefix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            result += self.prefix[row1 - 1][col1 - 1]

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)