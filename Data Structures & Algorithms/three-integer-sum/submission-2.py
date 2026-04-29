class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return triplets
                
        