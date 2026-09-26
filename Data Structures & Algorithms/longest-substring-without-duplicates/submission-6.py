"""
Time complexity: O(N)
Space complexity: O(1)
Time: 3min
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqs = defaultdict(int)
        max_len = 0
        left = 0
        n = len(s)
        for right in range(n):
            freqs[s[right]] += 1

            while freqs[s[right]] > 1:
                freqs[s[left]] -= 1
                left += 1
        
            max_len = max(max_len, right - left + 1)
        
        return max_len
        