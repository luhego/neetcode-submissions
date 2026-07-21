"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_unique = 1
        i, n = 1, len(nums)
        while i < n:
            if nums[i] != nums[i - 1]:
                nums[next_unique] = nums[i]
                next_unique += 1
            i += 1
        
        return next_unique
