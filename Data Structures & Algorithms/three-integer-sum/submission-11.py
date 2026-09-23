"""
Time complexity: O(N^2)
Space complexity: O(K), K is complexity of sorting algorithm N for Python TimSort
Time: 6min
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        nums.sort()

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets
