"""
N: number of words
L: max word length
Time complexity: O(N * L)
Space complexity: O(N * L)
Time: 5min
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def computeKey(word):
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            return tuple(key)

        groups = defaultdict(list)

        for word in strs:
            key = computeKey(word)
            groups[key].append(word)
        
        return list(groups.values())