from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        right_bracket, left_bracket = n, n
        self.acc, self.answer = "", []
        self.backTracking(right_bracket, left_bracket)
        return self.answer

    def backTracking(self, right_bracket, left_bracket):
        key = str(right_bracket) + "|" + str(left_bracket)
        if left_bracket > right_bracket:
            return
        elif right_bracket <= 0 and left_bracket <= 0:
            self.answer.append(self.acc)
            return

        next = [")", "("]
        for i in range(len(next)):
            self.acc += next[i]

            if i == 0 and right_bracket > 0:
                self.backTracking(right_bracket - 1, left_bracket)
            elif i == 1 and left_bracket > 0:
                self.backTracking(right_bracket, left_bracket - 1)

            self.acc = self.acc[:len(self.acc) - 1]



n = 3
solution = Solution()
print(solution.generateParenthesis(n))