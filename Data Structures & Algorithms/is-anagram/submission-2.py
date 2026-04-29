class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        s_map = defaultdict(int)
        for char in s:
            s_map[char] += 1

        for char in t:
            if char not in s_map:
                return False

            s_map[char] -= 1

            if s_map[char] < 0:
                return False

        return True