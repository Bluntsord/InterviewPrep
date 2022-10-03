from typing import *


class Solution:
    def deleteString(self, s: str) -> int:
        self.s = s
        self.memo = {}
        answer = self.dp(s)
        return answer

    def dp(self, string):
        if len(string) < 2:
            return 1
        elif string in self.memo:
            return self.memo[string]

        char_dict = dict(Counter(string))
        if len(char_dict) == 1:
            return char_dict[string[0]]
        answer, acc = 0, False
        for i in range(1, len(string) // 2 + 1):
            if char_dict[string[i]] == 1:
                break
            result, leftover_string = self.check_string(string, i)
            acc = result or acc
            if result:
                answer = max(answer, 1 + self.dp(leftover_string))

        if not acc:
            answer += 1

        self.memo[string] = answer
        return answer



    def check_string(self, string, length):
        curr = string[:length]
        result = string[:length] == string[length: length * 2]
        left_over = string[length:]
        return result, left_over

s = "aaaa"
solution = Solution()
print(solution.deleteString(s))