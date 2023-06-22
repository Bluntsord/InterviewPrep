from typing import *

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter, longer = str1, str2
        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        for curr_length in reversed(range(len(shorter) + 1)):
            for i in range(len(shorter) - curr_length + 1):
                curr_word = shorter[i: i + curr_length]
                if curr_word in longer:
                    return curr_word

        return ""

solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))


