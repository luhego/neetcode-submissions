"""
N: number of words
M: largest size of a word
Time complexity: O(N * M)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        stop = False
        i = 0
        while not stop:
            if i >= len(strs[0]):
                stop = True
                continue
    
            char = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    stop = True
                    break
            
            if stop:
                continue

            prefix.append(char)
        
            i += 1
        
        return "".join(prefix)