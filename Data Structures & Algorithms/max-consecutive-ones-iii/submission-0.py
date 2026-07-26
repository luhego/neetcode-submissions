"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        ones_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ones_count += 1

            while ones_count + k < right - left + 1:
                if nums[left] == 1:
                    ones_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        