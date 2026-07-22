"""
Time complexity: O(N)
Space complexity: O(1)
Time: 22min
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(i):
            start = i
            prev = nums[i]
            while True:
                j = (i + k) % n
                temp = nums[j]
                nums[j] = prev
                prev = temp
                i = j

                hm["counter"] += 1

                if i == start:
                    break

        hm = {"counter": 0}
        n = len(nums)
        k = k % n
        for i in range(n):
            if hm["counter"] < n:
                rotate(i)
            else:
                break