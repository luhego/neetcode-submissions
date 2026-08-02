"""
Time complexity: O(N*N!)
Space complexity: O(N*N!)
Time: 7min
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, curr_perm):
            if i == n:
                permutations.append(curr_perm[:])
                return

            for j in range(n):
                num = nums[j]
                if seen[num]:
                    continue

                seen[num] = True
                curr_perm.append(num)

                backtrack(i + 1, curr_perm)

                seen[num] = False
                curr_perm.pop()


        n = len(nums)
        permutations = []
        seen = defaultdict(bool)
        backtrack(0, [])
        return permutations
