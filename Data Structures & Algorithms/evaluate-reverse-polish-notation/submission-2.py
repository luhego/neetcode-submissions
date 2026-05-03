"""
Time complexity: O(N)
Space complexity: O(N)
Time: 4min
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

        operators = ["+", "-", "*", "/"]

        stack = []
        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(evaluate(op1, op2, token))
            else:
                stack.append(int(token))
        
        return stack[0]
       