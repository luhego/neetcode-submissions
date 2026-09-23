"""
Time complexity: O(N)
Space complexity: O(N)
Time: 12min
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 0
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum == k:
                count += 1

            diff = curr_sum - k
            if diff in seen:
                count += seen[diff]
            
            seen[curr_sum] += 1
        
        return count
