class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(int)

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in index:
                return [index[diff], idx]
            index[num] = idx

        return [-1, -1]
