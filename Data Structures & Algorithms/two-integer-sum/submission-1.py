"""
N: size of array nums
Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], i]

            visited[num] = i

        return [-1, -1]
        