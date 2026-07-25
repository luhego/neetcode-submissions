from functools import lru_cache

"""
Time complexity: O(N)
Space complexity: O(N)
Time: 8min
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache
        def traverse(i):
            if i >= n - 1:
                return 0

            min_jumps = float("inf")
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + traverse(i + j))

            return min_jumps

        n = len(nums)
        return traverse(0)