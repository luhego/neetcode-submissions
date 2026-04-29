class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        next_zero = 0
        next_two = n - 1
        i = 0
        while i <= next_two:
            if nums[i] == 0:
                nums[i], nums[next_zero] = nums[next_zero], nums[i]
                next_zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[next_two] = nums[next_two], nums[i]
                next_two -= 1
