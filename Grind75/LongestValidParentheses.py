from typing import *


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        answer = 0

        for i in range(len(s)):
            if s[i] == ")":
                prev_coord = stack.pop()
                answer = max(answer, i - prev_coord + 1)
            else:
                stack.append(i)

        return answer
