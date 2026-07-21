"""
Time complexity: O(NlogN) + O(N^2) = O(N^2)
Space complexity: O(1)
Time: 12min
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left -= 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return triplets
