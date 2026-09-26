"""
Time complexity: O(S + T)
Space complexity: O(1)
Time: 11min
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = defaultdict(int)
        for char in t:
            freqs[char] += 1

        n = len(s)
        left = 0
        min_len = n
        min_str = ""
        matches = 0
        for right in range(n):
            right_char = s[right]
            if right_char in freqs:
                freqs[right_char] -= 1
                if freqs[right_char] == 0:
                    matches += 1

            while matches == len(freqs):
                window_size = right - left + 1
                if window_size <= min_len:
                    min_len = window_size
                    min_str = s[left:right + 1]
                
                left_char = s[left]
                if left_char in freqs:
                    freqs[left_char] += 1
                    if freqs[left_char] == 1:
                        matches -= 1
                
                left += 1
        
        return min_str