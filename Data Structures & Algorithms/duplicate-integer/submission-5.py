"""
Time complexity: O(N)
Space complexity: O(N)
Time: 2min
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

