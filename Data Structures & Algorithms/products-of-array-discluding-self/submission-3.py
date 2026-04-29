"""
N is the number of elements of nums
output[i] where 0 <= i < N is left[i] * right[i] where
left[i]: product of all elements from index 0 to i - 1
right[i]: product of all elements from index i + 1 to N - 1
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        left_product = 1
        for i in range(n):
            left_product = nums[i - 1] * left_product if i > 0  else left_product
            output[i] = left_product

        right_product = 1
        for i in range(n - 1, -1, -1):
            right_product = nums[i + 1] * right_product if i < n - 1 else right_product
            output[i] = output[i] * right_product

        return output