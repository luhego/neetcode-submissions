"""
Time complexity: O(logx)
Space complexity: O(1)
Time: 3min
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x

        answer = 1
        while low <= high:
            mid = (low + high) // 2

            candidate = mid * mid
            if candidate == x:
                return mid
            elif candidate < x:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer
