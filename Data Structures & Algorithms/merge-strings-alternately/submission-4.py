"""
Time complexity: O(N + M)
Space complexity: O(1)
Time: 3min
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2 = 0, 0
        n1, n2 = len(word1), len(word2)

        result = []
        while i1 < n1 or i2 < n2:
            if i1 < n1:
                result.append(word1[i1])
                i1 += 1
            if i2 < n2:
                result.append(word2[i2])
                i2 += 1
        
        return "".join(result)