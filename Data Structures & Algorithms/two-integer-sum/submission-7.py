"""
Time complexity: O(N)
Space complexity: O(N)
Time: 2min
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
        
        return [-1, -1]