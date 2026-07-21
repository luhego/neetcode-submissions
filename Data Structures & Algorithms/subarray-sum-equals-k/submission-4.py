"""
Time complexity: O(N)
Space complexity: O(N)
Time: 13min
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = defaultdict(int)
        prefix = 0
        for num in nums:
            prefix += num
            if prefix == k:
                count += 1

            diff = prefix - k
            count += seen[diff]

            seen[prefix] += 1
        
        return count
