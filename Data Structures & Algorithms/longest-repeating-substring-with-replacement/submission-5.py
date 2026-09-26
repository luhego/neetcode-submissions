"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        left = 0
        n = len(s)
        max_freq = 0
        max_len = 0
        for right in range(n):
            freqs[s[right]] += 1
            max_freq = max(max_freq, freqs[s[right]])

            while max_freq + k < (right - left + 1):
                freqs[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len
