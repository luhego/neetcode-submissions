class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        unique_index = 0
        i = 0
        while i < n:
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        
            if i < n:
                nums[unique_index] = nums[i]
                unique_index += 1
                i += 1
        
        return unique_index