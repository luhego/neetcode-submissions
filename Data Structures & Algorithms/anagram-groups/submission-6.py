"""
N: number words:
W: largest length of a word

Time complexity: O(N*W)
Space complexity: O(N*W)
Time: 4min
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            
            key_tuple = tuple(key)
            groups[key_tuple].append(word)

        return list(groups.values())