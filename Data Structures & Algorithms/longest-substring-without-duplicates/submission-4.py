"""
Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_freqs = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(n):
            right_char = s[right]
            char_freqs[right_char] += 1

            # Shrink the window if there are duplicates
            while char_freqs[right_char] > 1:
                left_char = s[left]
                char_freqs[left_char] -= 1
                if char_freqs[left_char] == 0:
                    del char_freqs[left_char]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        