from typing import *

class Solution:
    def __init__(self):
        self.operations = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.operations:
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(self.handle_operation(token, first_operand, second_operand))

        return int(stack[0])


    def handle_operation(self, operation, first_operand, second_operand):
        if operation == "+":
            return first_operand + second_operand
        elif operation == "-":
            return first_operand - second_operand
        elif operation == "*":
            return first_operand * second_operand
        return first_operand/second_operand