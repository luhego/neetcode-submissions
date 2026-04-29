class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_frequencies = defaultdict(int)
        largest_frequency = 0
        max_len = 0
        
        window_start = 0
        for window_end in range(len(s)):
            char_frequencies[s[window_end]] += 1

            largest_frequency = max(largest_frequency, char_frequencies[s[window_end]])
            while largest_frequency + k < window_end - window_start + 1:
                char_frequencies[s[window_start]] -= 1
                if char_frequencies[s[window_start]] == 0:
                    del char_frequencies[s[window_start]]
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)

        return max_len