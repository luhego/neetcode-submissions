"""
N: number of operations
Time complexity(per operation):
    - push: O(N)
    - pop: O(1) on average
    - top: O(1) on average
    - empty: O(1)
Space complexity: O(N)
Time: 12min

"""


from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque([])
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        size = len(self.queue) - 1
        while size > 0:
            self.queue.append(self.queue.popleft())
            size -= 1
        
    def pop(self) -> int:
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()