class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []

        index = 0
        should_continue = True
        while should_continue:
            if index >= len(strs[0]):
                should_continue = False
            else:
                char = strs[0][index]
                idx = 0
                while idx < len(strs) and should_continue:
                    s = strs[idx]
                    if index >= len(s) or s[index] != char:
                        should_continue = False
                    idx += 1

            if should_continue:
                common_prefix.append(char)

            index += 1

        return "".join(common_prefix)