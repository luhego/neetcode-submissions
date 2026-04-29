class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i - 1]

        cum_right = 1
        for i in range(n - 2, -1, -1):
            cum_right = cum_right * nums[i + 1]
            answer[i] = answer[i] * cum_right
        
        return answer
