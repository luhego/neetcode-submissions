"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            
            if nums[left] != val:
                left += 1
        
        return left
