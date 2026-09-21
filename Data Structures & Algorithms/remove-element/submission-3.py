"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_index = 0
        i = 0
        n = len(nums)
        while i < n:
            while i < n and nums[i] == val:
                i += 1
            
            if i < n:
                nums[next_index] = nums[i]
                next_index += 1
                i += 1
        
        return next_index

