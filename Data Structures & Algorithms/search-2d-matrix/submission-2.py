"""
Solution A: Binary search on each row
Time complexity: O(MlogN)
Time: 4min

Solution B: Binary search over 1D array
Time complexity: O(logMN)
Time: 7min
    row = idx // n
    col = idx % n
    0   (0, 0)
    1   (0, 1)
    2   (0, 2)
    3   (0, 3)
    4   (1, 0)
    5   (1, 1)
    6   (1, 2)
    7   (1, 3)
    8   (2, 0)
    9   (2, 1)
    10  (2, 2)
    11  (2, 3)

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution A:
        # def binarySearch(row):
        #     low = 0
        #     high = n - 1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return False

        
        # m, n = len(matrix), len(matrix[0])
        # for row in matrix:
        #     found = binarySearch(row)
        #     if found:
        #         return True

        m, n = len(matrix), len(matrix[0])
        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
        