"""
Time complexity: O(N)
Space complexity: O(1)
Time: 25min
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        count = 0
        while count < n:
            curr_index, prev = start, nums[start]

            while True:
                next_index = (curr_index + k) % n
                nums[next_index], prev = prev, nums[next_index]
                curr_index = next_index
                count += 1
                if curr_index == start:
                    break
                
            start += 1
