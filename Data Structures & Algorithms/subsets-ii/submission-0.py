"""
2 branches, depth: N
Time complexity: O(N*2^N) -> N: cost of coyping, 2^N, number of calls to generateSubset
Space complexity:
    - Auxiliar: O(N)
    - Total: O(N*2^N) -> number of subsets(2^N) * max size of a subset(N)
Time: 9min
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def generateSubsets(i, curr_subset):
            if i == n:
                subsets.append(curr_subset[:])
                return
            if i > n:
                return

            curr_subset.append(nums[i])
            generateSubsets(i + 1, curr_subset)

            used = nums[i]
            while i < n - 1 and nums[i + 1] == used:
                i += 1

            curr_subset.pop()
            generateSubsets(i + 1, curr_subset)

        nums.sort()
        n = len(nums)
        subsets = []
        generateSubsets(0, [])
        return subsets
