"""
Time complexity: O(N)
Space complexity: O(1)
Time: 2min
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        votes = 0

        for num in nums:
            if candidate is None:
                candidate = num
                votes = 1
            elif num == candidate:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    candidate = num
                    votes = 1
            
        return candidate