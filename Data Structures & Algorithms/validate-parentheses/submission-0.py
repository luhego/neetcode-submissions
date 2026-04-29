class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0 or closing[char] != stack[-1]:
                    return False

                stack.pop() 

        return len(stack) == 0
