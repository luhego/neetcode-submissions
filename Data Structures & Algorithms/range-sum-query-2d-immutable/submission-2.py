"""
Approach A: Brute Force
Time complexity: O(M*N)
Space complexity: O(1)
Time: 7min

Approach B: Prefix Sum

Compute a prefix matrix where prefix(i, j) is
equal to the sum of the whole rectanble with indices (0,0) and (i, j).

To compute the sum of any rectangle with coordinates: (r1, c1) and (r2, c2)
This will be equal to prefix(r2,c2) - prefix(r2, c1 - 1) - prefix(r1 - 1, c2) + matrix(r1 - 1, c1 - 1)

Time complexity: O(1) per query
Space complexity: O(M*N)
Time: 26min
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.prefix = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                self.prefix[row][col] = matrix[row][col]
                self.prefix[row][col] -= self.prefix[row - 1][col - 1] if row > 0 and col > 0 else 0
                self.prefix[row][col] += self.prefix[row][col - 1] if col > 0 else 0
                self.prefix[row][col] += self.prefix[row - 1][col] if row > 0 else 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_sum = self.prefix[row2][col2]
        curr_sum -= self.prefix[row2][col1 - 1] if col1 > 0 else 0
        curr_sum -= self.prefix[row1 - 1][col2] if row1 > 0 else 0
        curr_sum += self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return curr_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)