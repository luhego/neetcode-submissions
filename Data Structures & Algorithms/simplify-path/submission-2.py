class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0
        n = len(path)
        while i < n:
            if path[i] == "/":
                if not stack or stack[-1] != "/":
                    stack.append(path[i])
                i += 1
            else:
                only_periods = True
                directory = []
                while i < n and (path[i].isalpha() or path[i] == "_" or path[i] == "."):
                    if path[i].isalpha() or path[i] == "_":
                        only_periods = False

                    directory.append(path[i])
                    i += 1

                if only_periods:
                    periods_len = len(directory)
                    if periods_len == 1:
                        continue
                    elif periods_len == 2:
                        if len(stack) > 1:
                            stack.pop() # Remove /
                        if stack:
                            stack.pop() # Move to the parent
                        continue
                stack.append("".join(directory))
        
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack)
