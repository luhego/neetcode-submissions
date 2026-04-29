"""
Time complexity: O(N)
Space complexity: O(N
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]

            seen[num] = i

        # It should never reach this line
        return [-1, -1]      