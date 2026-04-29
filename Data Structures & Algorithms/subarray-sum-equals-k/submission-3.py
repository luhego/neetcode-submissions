"""
nums=[1,-1,0]
k=0
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_subarrays = 0

        counter = defaultdict(int)
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum == k:
                num_subarrays += 1
            if curr_sum - k in counter:
                # look for a value x such as: curr_sum - x = k => x = curr_sum - k
                num_subarrays += counter[curr_sum - k]
            counter[curr_sum] += 1
        
        return num_subarrays

        