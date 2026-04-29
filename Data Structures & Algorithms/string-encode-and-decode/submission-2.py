from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        n = len(strs)
        result = []

        for word in strs:
            result.append(f"{len(word)}/:{word}")

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        n = len(s)
        i = 0
        while i < n:
            j = s.find("/:", i)
            word_len = int(s[i:j])
            result.append(s[j+2:j+2+word_len])
            i = j + 2 + word_len

        return result