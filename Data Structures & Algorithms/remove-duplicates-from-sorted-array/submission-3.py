"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_index = 0
        n = len(nums)
        i = 0
        while i < n:
            while 0 < i < n and nums[i] == nums[i - 1]:
                i += 1

            if i < n:
                nums[next_index] = nums[i]
                next_index += 1
            i += 1

        return next_index