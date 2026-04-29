class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window_start = 0
        freqs = defaultdict(int)
        for window_end in range(len(s)):
            freqs[s[window_end]] += 1

            while freqs[s[window_end]] > 1:
                freqs[s[window_start]] -= 1
                if freqs[s[window_start]] == 0:
                    del freqs[s[window_start]]
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)

        return max_len