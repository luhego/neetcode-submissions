"""
Time complexity: O(1) for each operation
Space complexity: O(N)
Time: 5min
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = val
        if self.stack:
            cur_min = min(cur_min, self.stack[-1][1])
        self.stack.append((val, cur_min))        

    def pop(self) -> None:
        return self.stack.pop()[0]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
