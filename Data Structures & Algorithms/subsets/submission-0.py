"""
Time complexity: O(N*2^N)
Space complexity: O(N)
Time: 3min
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(i, curr_set):
            if i == n:
                result.append(curr_set[:])
                return

            curr_set.append(nums[i])
            backtracking(i + 1, curr_set)

            curr_set.pop()
            backtracking(i + 1, curr_set)

        n = len(nums)
        result = []
        backtracking(0, [])
        return result