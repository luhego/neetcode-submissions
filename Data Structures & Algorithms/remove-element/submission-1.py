class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n - 1

        i = 0
        while i <= right:
            if nums[i] == val:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

            if nums[i] != val:
                i += 1
        
        return i
