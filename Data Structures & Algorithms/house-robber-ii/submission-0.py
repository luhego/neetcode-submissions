class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # Case 1, we rob house 0, so we don't include last house
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        result_1 = dp[n - 2]

        # Case 2, we skip house 0
        dp = [0] * n
        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        result_2 = dp[n - 1]

        return max(result_1, result_2)