"""
Time complexity: O(N)
Space complexity: O(N)
Time: 15min
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i, n = 0, len(s)
        while i < n:
            if s[i].isdigit():
                curr_k = []
                while i < n and s[i].isdigit():
                    curr_k.append(s[i])
                    i += 1
                
                # Add k to the stack
                stack.append("".join(curr_k))
            elif s[i].isalpha():
                curr_w = []
                while i < n and s[i].isalpha():
                    curr_w.append(s[i])
                    i += 1
                
                # Add w to the stack
                stack.append("".join(curr_w))
            elif s[i] == "[":
                stack.append(s[i])
                i += 1
            else:
                combined_w = deque([])
                while stack and stack[-1] != "[":
                    w = stack.pop()
                    combined_w.appendleft(w)
                w = "".join(combined_w)
        
                stack.pop() # Remove "["
                k = stack.pop()
                stack.append(w * int(k))
                i += 1
        
        return "".join(stack)
        