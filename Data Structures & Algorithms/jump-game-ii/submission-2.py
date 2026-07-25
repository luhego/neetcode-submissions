from functools import lru_cache

"""
Solution A: DP
Time complexity: O(N^2)
Space complexity: O(N)
Time: 8min

Solution B: Greedy
Time complexity: O(N)
Space complexity: O(1)
Time: 15min
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # @lru_cache
        # def traverse(i):
        #     if i >= n - 1:
        #         return 0

        #     min_jumps = float("inf")
        #     for j in range(1, nums[i] + 1):
        #         min_jumps = min(min_jumps, 1 + traverse(i + j))

        #     return min_jumps

        # n = len(nums)
        # return traverse(0)

        n = len(nums)
        count = 0
        left, right = 0, 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            
            left = right + 1
            right = farthest
            count += 1
        
        return count
