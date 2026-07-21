"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_unique = 0
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i] != nums[i + 1]:
                nums[next_unique], nums[i] = nums[i], nums[next_unique]
                next_unique += 1
            i += 1
        
        nums[next_unique], nums[i] = nums[i], nums[next_unique]
        next_unique += 1
        
        return next_unique
