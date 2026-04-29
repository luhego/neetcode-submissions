"""
S: size of string s
T: size of string T
M: max(S, T)

Time complexity: O(S + T)
Space complexity: O(26) -> O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_frequencies = defaultdict(int)
        for char in s:
            char_frequencies[char] += 1


        for char in t:
            if char not in char_frequencies:
                return False

            char_frequencies[char] -= 1
            if char_frequencies[char] == 0:
                del char_frequencies[char]

        return True