"""
Time complexity: O(N2^N)
Space complexity: O(N)
Time: 17min
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtracking(i, curr_subset, curr_sum):
            if curr_sum > target:
                return

            if i == n:
                if curr_sum == target:
                    result.append(curr_subset[:])
                return

            curr_subset.append(nums[i])
            backtracking(i, curr_subset, curr_sum + nums[i])
            curr_subset.pop()

            backtracking(i + 1, curr_subset, curr_sum)

        n = len(nums)
        result = []
        backtracking(0, [], 0)
        return result
