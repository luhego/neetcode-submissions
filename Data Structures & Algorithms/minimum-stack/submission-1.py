class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            min_val = min(val, self.stack[-1][1])
            self.stack.append((val, min_val))

    def pop(self) -> None:
        val, _ = self.stack.pop()
        return val        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
