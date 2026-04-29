class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left_index = 0
        right_index = n - 1
        index = 0

        while index <= right_index:
            if nums[index] == 0:
                nums[left_index], nums[index] = nums[index], nums[left_index]
                left_index += 1
                index += 1
            elif nums[index] == 2:
                nums[right_index], nums[index] = nums[index], nums[right_index]
                right_index -= 1
            else:
                index += 1
