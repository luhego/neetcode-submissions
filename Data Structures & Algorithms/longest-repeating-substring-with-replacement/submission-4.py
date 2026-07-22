"""
Time complexity: O(N)
Space complexity: O(N)
Time: 9min
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freqs = defaultdict(int)
        most_frequent = 0
        left = 0
        for right in range(len(s)):
            right_char = s[right]
            freqs[right_char] += 1
            most_frequent = max(most_frequent, freqs[right_char])

            while most_frequent + k < (right - left + 1):
                left_char = s[left]
                freqs[left_char] -= 1
                left += 1
        
            max_len = max(max_len, right - left + 1)
    
        return max_len
