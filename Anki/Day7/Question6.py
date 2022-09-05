from typing import *


class Solution:
    def numDecodings(self, s: str) -> int:
        self.num_dict = {str(i): chr(x) for i, x in enumerate(range(65, 91), 1)}
        self.answer = 0
        self.memo = {}
        answer = self.backTracking(s)

        return answer

    def backTracking(self, curr_string):
        if curr_string == "":
            return 1
        elif curr_string in self.memo:
            return self.memo[curr_string]

        neighbours = {curr_string[0], curr_string[0:2]}

        answer = 0
        for neighbour in neighbours:
            if neighbour in self.num_dict:
                next_string = curr_string[len(neighbour):]

                answer += self.backTracking(next_string)

        self.memo[curr_string] = answer
        return answer



s = "111111111111111111111111111111111111111111111111"
solution = Solution()
print(solution.numDecodings(s))