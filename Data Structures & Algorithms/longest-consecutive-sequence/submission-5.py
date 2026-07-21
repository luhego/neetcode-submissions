"""
Time complexity: O(N)
Space complexity: O(N)
Time: 5min
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_len = 0
        for num in nums:
            if (num - 1) in seen:
                continue
            
            curr_len = 0
            while num in seen:
                curr_len += 1
                num += 1
            
            max_len = max(max_len, curr_len)
    
        return max_len