"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1
        
        for char in t:
            if char not in freqs:
                return False
            freqs[char] -= 1
            if freqs[char] == 0:
                del freqs[char]
        
        return True
