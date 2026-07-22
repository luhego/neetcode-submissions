"""
Time complexity: O(N)
Space complexity: O(N)
Time: 4min
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = defaultdict(int)
        for i in range(n):
            num = nums[i]
            if num in seen and abs(i - seen[num]) <= k:
                return True
            seen[num] = i
        return False
