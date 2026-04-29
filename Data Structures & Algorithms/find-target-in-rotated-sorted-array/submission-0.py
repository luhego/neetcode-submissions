class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2

                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        def find_peak():
            low = 0
            high = n - 1

            while low < high:
                mid = (low + high)
                if nums[mid] < nums[0]:
                    high = mid - 1
                else:
                    low = mid

            return low

        n = len(nums)
        # no rotation
        if nums[-1] > nums[0]:
            return binary_search(0, n - 1)
        else:
            index = find_peak()
            if target >= nums[0] and target <= nums[index]:
                return binary_search(0, index) 
            else:
                return binary_search(index + 1, n - 1)
