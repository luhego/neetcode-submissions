"""
Time complexity: O(2 ^ N)
Space complexity: O(K)
Time: 6min
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, curr_combination):
            if len(curr_combination) == k:
                combinations.append(curr_combination[:])
                return

            if i > n:
                return

            curr_combination.append(i)
            backtrack(i + 1, curr_combination)
            curr_combination.pop()

            backtrack(i + 1, curr_combination)
        
        combinations = []
        backtrack(1, [])
        return combinations
