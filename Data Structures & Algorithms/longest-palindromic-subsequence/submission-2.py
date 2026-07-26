"""
Time complexity: O(N^2)
Space complexity: O(N^2)
Time: 9min
"""
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def traverse(start, end):
            if start == end:
                return 1
            elif start > end:
                return 0

            max_len = 1
            if s[start] == s[end]:
                return 2 + traverse(start + 1, end - 1)
            
            return max(traverse(start + 1, end), traverse(start, end - 1))

        return traverse(0, len(s) - 1)
        