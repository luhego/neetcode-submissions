"""
Time complexity: O(N + M)
Space complexity: O(1)
Time: 8min
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = m + n - 1
        i1, i2 = m - 1, n - 1
        while right >= 0:
            if i1 >= 0 and i2 >= 0:
                if nums1[i1] >= nums2[i2]:
                    nums1[right] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[right] = nums2[i2]
                    i2 -= 1
            elif i1 >= 0:
                nums1[right] = nums1[i1]
                i1 -= 1
            else:
                nums1[right] = nums2[i2]
                i2 -= 1
            
            right -= 1