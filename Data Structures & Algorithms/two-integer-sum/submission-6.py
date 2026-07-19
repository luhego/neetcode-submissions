"""
Time complexity: O(N)
Space complexity: O(N)
Time: 4min
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index:
                return [index[diff], i]
            index[num] = i
        
        return [-1, -1]
        