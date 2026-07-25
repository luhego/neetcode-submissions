
"""
Time complexity: O(logN)
Space complexity: O(1)
Time: 10min
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        if nums[low] <= nums[high]:
            return nums[low]

        answer = 0
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[n - 1]:
                low = mid + 1
            else:
                answer = nums[mid]
                high = mid - 1
        
        return answer