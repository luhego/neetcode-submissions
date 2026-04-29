class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        n = len(s)

        max_len = 0
        most_frequent = 0
        left = 0
        for right in range(n):
            right_char = s[right]
            freqs[right_char] += 1
            most_frequent = max(most_frequent, freqs[right_char])

            while left < n and right - left + 1 > most_frequent + k:
                left_char = s[left]
                freqs[left_char] -= 1
                if freqs[left_char] == 0:
                    del freqs[left_char]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
