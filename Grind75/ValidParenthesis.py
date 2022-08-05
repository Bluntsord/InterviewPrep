import typing


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in dict.values():
                stack.append(i)
            elif len(stack) != 0 and i in dict.keys() and dict[i] == stack[-1]:
                stack.pop()
        return len(stack) == 0
