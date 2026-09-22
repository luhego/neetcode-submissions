"""
Time complexity: O(N)
Space complexity: O(N)
Time: 15min
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for word in strs:
            encoded_str.append(str(len(word)) + "#" + word)
        
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            sep_index = s.index("#", i)
            word_len = int(s[i:sep_index])
            word = s[sep_index + 1: sep_index + word_len + 1]
            decoded.append(word)
            i = sep_index + word_len + 1
        
        return decoded