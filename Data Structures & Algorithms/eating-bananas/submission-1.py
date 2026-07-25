"""
Time complexity: O(logN)
Space complexity: O(1)
Time: 12min
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBananasWithinH(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile // k)
                if pile % k > 0:
                    total_hours += 1
                if total_hours > h:
                    return False
            return True

        low = 1
        high = max(piles)

        answer = 0
        while low <= high:
            mid = (low + high) // 2

            if canEatBananasWithinH(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer