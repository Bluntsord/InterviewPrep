from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.stack = []
        self.answer = []
        self.neighbours = ["(", ")"]
        self.helper(n, n)
        return self.answer

    def helper(self, open_bracket, close_bracket):
        # Early prunning of bracket
        if close_bracket < open_bracket:
            return
        elif close_bracket < 0 or open_bracket < 0:
            return
        elif open_bracket == 0 and close_bracket == 0:
            curr = ''.join(self.stack)
            self.answer.append(curr)
            return

        for neighbour in self.neighbours:
            self.stack.append(neighbour)

            if neighbour == "(":
                self.helper(open_bracket - 1, close_bracket)
            else:
                self.helper(open_bracket, close_bracket - 1)

            self.stack.pop()

solution = Solution()
print(solution.generateParenthesis(4))