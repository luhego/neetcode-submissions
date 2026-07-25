"""
Time complexity: O(N)
Space complexity: O(1)
Time: 14min
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        end = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0