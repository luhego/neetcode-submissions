"""
Time complexity: O(N)
Space complexity: O(N)
Time: 4mins
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left_product = 1
        for i, num in enumerate(nums):
            result[i] = left_product
            left_product *= num
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
        