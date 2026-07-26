"""
Time complexity: O(N)
Space complexity: O(1)
Time; 13min
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        left = 0

        total_satisfied = sum(customers[i] if grumpy[i] == 0 else 0 for i in range(n))
        max_satisfied = total_satisfied

        curr_satisfied = 0
        actual_satisfied = 0
        for right in range(n):
            curr_satisfied += customers[right]
            actual_satisfied += (customers[right] if grumpy[right] == 0 else 0)

            if right - left + 1 == minutes:
                max_satisfied = max(max_satisfied, total_satisfied - actual_satisfied + curr_satisfied)
                curr_satisfied -= customers[left]
                actual_satisfied -= (customers[left] if grumpy[left] == 0 else 0)
                
                left += 1
        return max_satisfied
