class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return triplets