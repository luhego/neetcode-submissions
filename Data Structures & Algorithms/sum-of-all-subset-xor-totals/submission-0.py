"""
Time complexity: O(2^N)
Space complexity: O(N)
Time: 18min
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subsets(i, curr_set, xor_total):
            if i == n:
                self.total_sum += xor_total
                return

            # Take the current element
            curr_set.append(nums[i])
            subsets(i + 1, curr_set, xor_total ^ nums[i])

            # Skip the current element
            curr_set.pop()
            subsets(i + 1, curr_set, xor_total)

        self.total_sum = 0
        n = len(nums)
        subsets(0, [], 0)        
        return self.total_sum
