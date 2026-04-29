class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 1

        for i in range(1, len(nums)):
            num = nums[i]

            if num == candidate:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    candidate = num
                    votes = 1

        return candidate
