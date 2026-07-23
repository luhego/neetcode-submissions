"""
Time complexity: O(N)
Space complexity: O(1) -> at most two values in the stack for a valid arithmetic
expression in polish notation
Time: 5min
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(op1, op2, operator):
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            else:
                return int(op1 / op2)

        answer = 0
        stack = []
        for token in tokens:
            if token in "+-*/":
                op2 = stack.pop()
                op1 = stack.pop()
                result = evaluate(op1, op2, token)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]
        