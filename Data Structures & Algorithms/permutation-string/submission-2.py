class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        freqs_1 = defaultdict(int)
        for char in s1:
            freqs_1[char] += 1

        freqs_2 = defaultdict(int)
        left = 0
        for right in range(n2):
            right_char = s2[right]
            freqs_2[right_char] += 1
            while left <= right and (right_char not in freqs_1 or freqs_2[right_char] > freqs_1[right_char]):
                left_char = s2[left]
                freqs_2[left_char] -= 1
                if freqs_2[left_char] == 0:
                    del freqs_2[left_char]
                left += 1

            if right - left + 1 == n1:
                return True

        return False
