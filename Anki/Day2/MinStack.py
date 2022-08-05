from typing import *


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr = (val, min(self.getMin(), val))
        self.stack.append(curr)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float('inf')
        return self.stack[len(self.stack) - 1][1]
