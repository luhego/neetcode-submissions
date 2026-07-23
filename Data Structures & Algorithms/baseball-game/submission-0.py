"""
Time complexity: O(N)
Space complexity: O(N)
Time: 3min
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            elif operation == "D":
                stack.append(2 * stack[-1])
            elif operation == "C":
                stack.pop()
            else:
                x = int(operation)
                stack.append(x)
    
        return sum(stack)