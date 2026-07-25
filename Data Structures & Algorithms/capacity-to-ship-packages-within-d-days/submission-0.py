"""
Time complexity: O(logN)
Space complexity: O(1)
Time: 20min
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canLoadWeights(capacity):
            curr_days = 0
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight <= capacity:
                    curr_weight += weight
                else:
                    curr_days += 1
                    curr_weight = weight

            if curr_weight > 0:
                curr_days += 1
            
            return curr_days <= days

        low = max(weights)
        high = sum(weights)

        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if canLoadWeights(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
