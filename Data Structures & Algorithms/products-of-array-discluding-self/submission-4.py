"""
Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * (n)

        # Compute the total product of all elements from index 0 to i - 1
        cum_product = 1
        for i in range(n):
            answer[i] = cum_product
            cum_product *= nums[i]

        # Compute the product of elements to the right
        cum_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= cum_product
            cum_product *= nums[i]

        return answer