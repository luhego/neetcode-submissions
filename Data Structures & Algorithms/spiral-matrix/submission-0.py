"""
Time complexity: O(MN)
Space complexity: O(1)
Time: 18min
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 1, m - 1
        left, right = 0, n - 1

        direction = "R"
        next_direction = {"R": "B", "B": "L", "L": "U", "U": "R"}
        answer = []
        i, j = 0, 0
        while len(answer) < m * n:
            if direction == "R":
                while j <= right:
                    answer.append(matrix[i][j])
                    j += 1
                i += 1
                j -= 1
                right -= 1
            elif direction == "B":
                while i <= bottom:
                    answer.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                bottom -= 1
            elif direction == "L":
                while j >= left:
                    answer.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                left += 1
            else:
                while i >= top:
                    answer.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                top += 1
            
            direction = next_direction[direction]

        return answer