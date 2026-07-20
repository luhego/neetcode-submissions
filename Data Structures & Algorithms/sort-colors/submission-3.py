"""
Time complexity: O(N)
Space complexity: O(1)
Time: 8min
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_idx = 0
        two_idx = n - 1
        idx = 0
        while idx <= two_idx:
            if nums[idx] == 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[two_idx] = nums[two_idx], nums[idx]
                two_idx -= 1
            else:
                idx += 1

        