"""
Time complexity: O(NlogN + T/min_c)
Time: 30min
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, curr_subset, curr_sum):
            if curr_sum == target:
                result.append(curr_subset.copy())
                return

            if curr_sum > target or i >= len(candidates):
                return

            curr_subset.append(candidates[i])
            backtrack(i + 1, curr_subset, curr_sum + candidates[i])
            curr_subset.pop()

            # Since we took candidates[i], we need to make sure we skip all duplicates
            used = candidates[i]
            while i < len(candidates) - 1 and candidates[i + 1] == used:
                i += 1

            backtrack(i + 1, curr_subset, curr_sum)
    
        candidates.sort()
        result = []
        backtrack(0, [], 0)
        return result