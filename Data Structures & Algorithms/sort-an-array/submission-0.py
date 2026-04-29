class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num, max_num = float("inf"), float("-inf")
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        i = 0
        for num in range(min_num, max_num + 1):
            while freqs[num] > 0:
                nums[i] = num
                freqs[num] -= 1
                i += 1

        return nums
