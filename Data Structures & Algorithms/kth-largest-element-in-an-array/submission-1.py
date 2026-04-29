import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[pivot_idx], nums[right]
            pivot = nums[right]
            p = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[p], nums[j] = nums[j], nums[p]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]
            return p


        def quickSelect(left, right):
            if left == right:
                return nums[left]

            pivot_index = partition(left, right)                
            if pivot_index > k:
                return quickSelect(left, pivot_index - 1)
            elif pivot_index < k:
                return quickSelect(pivot_index + 1, right)
            else:
                return nums[pivot_index]

        n = len(nums)
        k = n - k
        return quickSelect(0, n - 1)
        