from collections import defaultdict

"""
Time complexity: O(N)
Space complexity: O(26) ~ O(1)
Time: 5 mins
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1

        for c in t:
            # c only exists in t but not in s
            if c not in char_freq:
                return False

            char_freq[c] -= 1
            # c frequency in t > c frequency in s
            if char_freq[c] < 0:
                return False


        for c in s:
            # c frequency in s > c frequency in t
            if char_freq[c] > 0:
                return False
        
        return True