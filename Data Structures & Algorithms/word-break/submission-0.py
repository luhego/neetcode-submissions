"""
N: size of s
M: number of words in wordDict
Time complexity: O(MN^2)
Space complexity: O(N)
Time: 10min
"""

from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def traverse(i):
            if i == n:
                return True

            found = False
            for word in wordDict:
                word_len = len(word)
                if i + word_len > n:
                    continue

                if s[i: i + word_len] == word and traverse(i + word_len):
                    found = True
                    break

            return found

        n = len(s)
        return traverse(0)