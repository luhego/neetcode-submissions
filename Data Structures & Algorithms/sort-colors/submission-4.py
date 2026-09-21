"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_zero = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            elif nums[left] == 0:
                nums[next_zero], nums[left] = nums[left], nums[next_zero]
                next_zero += 1
                left += 1
            else:
                left += 1