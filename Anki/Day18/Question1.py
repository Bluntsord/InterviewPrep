from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token.isdigit():
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                next = self.handle_calculation(first_operand, second_operand, token)
                stack.append(next)
        return stack[0]

    def handle_calculation(self, first_operand, second_operand, operation):
        if operation == "+":
            return first_operand + second_operand
        elif operation == "-":
            return first_operand - second_operand
        elif operation == "/":
            return first_operand // second_operand
        else:
            return first_operand * second_operand

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(tokens))