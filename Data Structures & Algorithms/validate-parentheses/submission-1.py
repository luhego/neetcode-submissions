class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = "({["
        closed_chars = ")}]"

        stack = []
        for char in s:
            if char in open_chars:
                stack.append(char)
            else:
                idx = closed_chars.find(char)
                if not stack or stack[-1] != open_chars[idx]:
                    return False
                stack.pop()
        
        # stack should be empty
        return not stack