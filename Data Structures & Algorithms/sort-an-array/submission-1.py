"""
N: number of elements in the array
K: max value of each number
Time complexity: O(N)
Space complexity: O(K)
Time: 8min
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        ans = []
        for num in range(min_val, max_val + 1):
            while freqs[num] > 0:
                ans.append(num)
                freqs[num] -= 1
        
        return ans
        