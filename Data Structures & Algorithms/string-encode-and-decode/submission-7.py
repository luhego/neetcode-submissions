"""
Time complexity: O(M)
Space complexity: O(M+N)
Time: 60min
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)) + "#" + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            delimiter_idx = s.find("#", i)
            word_len = int(s[i:delimiter_idx])
            start, end = delimiter_idx + 1, delimiter_idx + 1 + word_len
            decoded.append(s[start:end])
            i = end

        return decoded
