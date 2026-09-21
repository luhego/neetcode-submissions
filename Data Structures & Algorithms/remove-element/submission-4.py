"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_index = 0
        for num in nums:
            if num != val:
                nums[next_index] = num
                next_index += 1
        
        return next_index

