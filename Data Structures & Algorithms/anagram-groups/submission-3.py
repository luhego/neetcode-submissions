class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def computeKey(word):
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1
            return key

        groups = defaultdict(list)

        for word in strs:
            key = computeKey(word)
            groups[tuple(key)].append(word)
            
        return list(groups.values())