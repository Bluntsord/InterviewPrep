from typing import *

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        self.memo = {}
        answer = self.dp(0, "#")
        return answer

    def dp(self, pointer, prev):
        key = str(pointer) + "|" + str(prev)
        if pointer >= len(self.s):
            return 0
        elif key in self.memo:
            return self.memo[key]

        curr = self.s[pointer]
        if self.absolute_diff_of_letters(curr, prev, self.k) or prev == "#":
            take_curr = 1 + self.dp(pointer + 1, curr)
        else:
            take_curr = -1
        drop_curr = self.dp(pointer + 1, prev)
        answer = max(take_curr, drop_curr)
        self.memo[key] = answer

        return answer

    def absolute_diff_of_letters(self, first_letter, second_letter, k):
        if -k <= ord(first_letter) - ord(second_letter) <= k:
            return True
        return False

first_str = "a"
second_str = "b"
third_str = "e"
s = "pvjcci"
k = 4
solution = Solution()
print(solution.longestIdealString(s, k))