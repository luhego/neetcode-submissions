"""
N: number of operations
Time complexity:
    - push: O(1)
    - pop: O(1) on average
    - peek: O(1)  on average
    - empty: O(1)
Space complexity: O(N)
Time: 10min

Approach:
We will have two stacks: s1 and s2
We will push all elements into the s1.
We will pop from stack s2. If s2 is empty, we move all elements from s1 to s2.
"""

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            self._move()
        
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            self._move()
        
        return self.s2[-1]

    def empty(self) -> bool:
        return (len(self.s1) + len(self.s2)) == 0
        
    def _move(self):
        while self.s1:
            self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()