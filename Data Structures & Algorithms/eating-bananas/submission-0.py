class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile // k)
                total_hours += (1 if pile % k != 0 else 0)
                if total_hours > h:
                    return False
            return True

        low = 1
        high = max(piles)
        
        while low < high:
            k = (low + high) // 2
            if canEatAllBananas(k):
                high = k
            else:
                low = k + 1

        return low