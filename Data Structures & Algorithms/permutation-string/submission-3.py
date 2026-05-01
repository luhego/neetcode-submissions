class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freqs = defaultdict(int)
        for char in s1:
            char_freqs[char] += 1

        left = 0
        num_matches = 0
        for right in range(len(s2)):
            right_char = s2[right]
            if right_char in char_freqs:
                char_freqs[right_char] -= 1
                if char_freqs[right_char] == 0:
                    num_matches += 1
            
            if num_matches == len(char_freqs):
                return True
        
            while left <= right and (right_char not in char_freqs or char_freqs[right_char] < 0):
                left_char = s2[left]
                if left_char in char_freqs:
                    char_freqs[left_char] += 1
                    if char_freqs[left_char] == 1:
                        num_matches -= 1
                left += 1

        return False