class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []

        curr_index = 0
        should_continue = True
        while should_continue:
            if curr_index >= len(strs[0]):
                should_continue = False
            else:
                candidate = strs[0][curr_index]
                for i in range(1, len(strs)):
                    if curr_index >= len(strs[i]) or strs[i][curr_index] != candidate:
                        should_continue = False
                        break

            if should_continue:
                common_prefix.append(candidate)
                curr_index += 1

        return "".join(common_prefix)