class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequencies = defaultdict(int)
        for char in s1:
            char_frequencies[char] += 1

        window_start =0
        for window_end in range(len(s2)):
            right_char = s2[window_end]

            if right_char in char_frequencies:
                char_frequencies[right_char] -= 1

            while window_start <= window_end and (right_char not in char_frequencies or char_frequencies[right_char] < 0):
                left_char = s2[window_start]
                if left_char in char_frequencies:
                    char_frequencies[left_char] += 1
                window_start += 1

            if window_end - window_start + 1 == len(s1):
                return True

        return False