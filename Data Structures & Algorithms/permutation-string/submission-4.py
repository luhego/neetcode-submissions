"""
Time complexity: O(N)
Space complexity: O(1)
Time: 10min
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs = defaultdict(int)
        for char in s1:
            freqs[char] += 1
        
        num_matches = 0
        left = 0
        for right in range(len(s2)):
            right_char = s2[right]
            if right_char in freqs:
                freqs[right_char] -= 1
                if freqs[right_char] == 0:
                    num_matches += 1
            
            if num_matches == len(freqs):
                return True

            while left <= right and (right_char not in freqs or freqs[right_char] < 0):
                left_char = s2[left]
                if left_char in freqs:
                    freqs[left_char] += 1
                    if freqs[left_char] == 1:
                        num_matches -= 1
                left += 1
        
        return False
       