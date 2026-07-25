"""
Solution A: Binary search on each row
Time complexity: O(MlogN)
Time: 4min
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row):
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            found = binarySearch(row)
            if found:
                return True
        
        return False
        