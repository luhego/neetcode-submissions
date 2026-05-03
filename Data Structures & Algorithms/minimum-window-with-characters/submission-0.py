"""
Time complexity: O(S + T)
Space complexity: O(T)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_freq = defaultdict(int)
        for char in t:
            chars_freq[char] += 1

        min_len = float("inf")
        min_str = ""
        num_matches = 0
        left = 0
        for right in range(len(s)):
            right_char = s[right]
            if right_char in chars_freq:
                chars_freq[right_char] -= 1
                if chars_freq[right_char] == 0:
                    num_matches += 1

            while left <= right and num_matches == len(chars_freq):
                if right - left + 1 < min_len:
                    min_len = min(min_len, right - left + 1)
                    min_str = s[left:right+1]

                left_char = s[left]
                if left_char in chars_freq:
                    chars_freq[left_char] += 1
                    if chars_freq[left_char] == 1:
                        num_matches -= 1

                left += 1
        
        return min_str

