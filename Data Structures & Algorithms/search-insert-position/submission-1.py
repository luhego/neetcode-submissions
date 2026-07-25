"""
Time complexity: O(logN)
Space complexity: O(1)
Time: 3min
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        candidate = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                candidate = mid + 1
                low = mid + 1
            else:
                high = mid - 1
        
        return candidate