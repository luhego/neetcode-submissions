"""
Time complexity: O(N)
Space complexity: O(N)
Time: 6min
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val = float("inf")
        max_val = float("-inf")
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
            min_val = min(min_val, num)
            max_val = max(max_val, num)

        i = 0
        for num in range(min_val, max_val + 1):
            while freqs[num] > 0:
                nums[i] = num
                freqs[num] -= 1
                i += 1

        return nums
