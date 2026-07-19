"""
Time complexity: O(N)
Space complexity: O(N) if considering ans array. O(1) otherwise
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans
       