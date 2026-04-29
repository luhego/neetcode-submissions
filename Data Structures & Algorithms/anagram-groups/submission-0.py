"""
"abcdz", hash(abcd) -> [1, 1, 1, 1, 0..., 1]

N: number of words
S: size of the word

Time complexity: O(N * S)
Space complexity: O(N * S)

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1

            anagram_groups[tuple(key)].append(word)

        return anagram_groups.values()
