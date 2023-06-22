from typing import *


class Solution:
    def partitionString(self, s: str) -> int:
        self.memo, self.s = {}, s
        return self.dp(0)

    def dp(self, pointer):
        if pointer >= len(self.s):
            return 0
        elif pointer in self.memo:
            return self.memo[pointer]

        curr_set = set()
        answer = float('inf')
        for i in range(pointer, len(self.s)):
            if self.s[i] in curr_set:
                answer = min(answer, 1 + self.dp(i))
                break
            else:
                curr_set.add(self.s[i])
                answer = min(answer, 1 + self.dp(i + 1))
        self.memo[pointer] = answer

        return answer


s = "abacabaAAAA"
solution = Solution()
print(solution.partitionString(s))