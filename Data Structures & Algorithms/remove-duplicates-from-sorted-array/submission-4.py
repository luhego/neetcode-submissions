"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_index = 1
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] != nums[i - 1]:
                nums[next_index] = nums[i]
                next_index += 1
            i += 1

        return next_index