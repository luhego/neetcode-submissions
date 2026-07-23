"""
N: number of operations
Time complexity(per operation):
    - push: O(1)
    - pop: O(1) on average
    - top: O(1) on average
    - empty: O(1)
Space complexity: O(N)
Time: 12min

Approach: 
We will have two queues: one will be empty and one will have elements.
- push: let's push the element to the back of the queue with elements
- pop: let's transfer all elements to the other queue and only keep one element
"""


from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
        
    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        
    def pop(self) -> int:
        if len(self.q1) > len(self.q2):
            self._move(self.q1, self.q2)
            return self.q1.popleft()
        else:
            self._move(self.q2, self.q1)
            return self.q2.popleft()
        
    def top(self) -> int:
        if len(self.q1) > len(self.q2):
            self._move(self.q1, self.q2)
            return self.q1[0]
        else:
            self._move(self.q2, self.q1)
            return self.q2[0]

    def _move(self, q1, q2):
        while len(q1) > 1:
            q2.append(q1.popleft())

    def empty(self) -> bool:
        total_len = len(self.q1) + len(self.q2)
        return total_len == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()