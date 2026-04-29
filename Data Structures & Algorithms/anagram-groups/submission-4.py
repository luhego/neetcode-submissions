"""
N: number of strings
M: average size of string
Time complexity: O(N * M)
Space complexity: O(N * M)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - 97] += 1
            groups_dict[tuple(key)].append(string)
        
        return list(groups_dict.values())
