from typing import *


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            curr = (val, val)
        else:
            curr = (val, min(self.stack[-1], val))
        self.stack.append(curr)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
