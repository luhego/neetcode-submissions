"""
Time complexity: O(logN)
Space complexity: O(1)
Time: 15min
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target:
                    if target <= nums[n - 1]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    high = mid - 1

        return -1
        