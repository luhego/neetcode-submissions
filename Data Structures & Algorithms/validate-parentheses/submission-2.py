"""
Time complexity: O(N)
Space complexity: O(N)
Time: 5min
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
    
        return len(stack) == 0