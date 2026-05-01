"""
Time complexity: O(N)
Space complexity: O(M)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_freqs = defaultdict(int)
        most_frequent = 0
        max_len = 0

        left = 0
        for right in range(n):
            right_char = s[right]
            char_freqs[right_char] += 1
            most_frequent = max(most_frequent, char_freqs[right_char])

            # Shrink current window
            while most_frequent + k < right - left + 1:
                left_char = s[left]
                char_freqs[left_char] -= 1
                if char_freqs[left_char] == 0:
                    del char_freqs[left_char]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
