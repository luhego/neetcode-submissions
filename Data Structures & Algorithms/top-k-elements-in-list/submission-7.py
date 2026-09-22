"""
N: number of elements in nums
R: max frequency of a number bounded by N
Time complexity: O(N + R) = O(N)
Space complexity: O(N)
Time: 6min
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = float("-inf")
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
            max_freq = max(max_freq, freqs[num])

        arr = [[] for _ in range(max_freq + 1)]
        for num, freq in freqs.items():
            arr[freq].append(num)

        result = []
        count = 0
        for freq in range(max_freq, -1, -1):
            for num in arr[freq]:
                result.append(num)
                count += 1

                if count == k:
                    return result
        
        return result
      
