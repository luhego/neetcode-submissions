"""
Time complexity: O(1) for each method
Space complexity: O(n)
Time: 4min
Approach: keep track of current min value every time we append a new element to the stack
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            cur_min = min(val, self.stack[-1][1])
            self.stack.append((val, cur_min))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
