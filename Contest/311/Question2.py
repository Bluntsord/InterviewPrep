from typing import *


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left_pointer, right_pointer = 1, 1
        answer = 1

        while right_pointer < len(s):
            while ord(s[right_pointer]) - ord(s[right_pointer - 1]) == 1:
                right_pointer += 1
                if right_pointer == len(s):
                    break
            answer = max(answer, right_pointer - left_pointer + 1)
            right_pointer += 1
            left_pointer = right_pointer

        return answer

s = "abacaba"
# s = "abcde"
solution = Solution()
print(solution.longestContinuousSubstring(s))

