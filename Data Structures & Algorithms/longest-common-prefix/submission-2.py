"""
N: number of words
L: max word length
Time complexity: O(NM)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
            
            i += 1
        
        return strs[0][:i]
