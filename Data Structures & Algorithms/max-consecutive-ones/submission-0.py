"""
Time complexity: O(N)
Space complexity: O(1)
Time: 2min
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                max_so_far = max(max_so_far, curr_count)
                curr_count = 0
        
        if curr_count:
            max_so_far = max(max_so_far, curr_count)
        
        return max_so_far

        