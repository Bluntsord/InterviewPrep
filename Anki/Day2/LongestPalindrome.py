from typing import *
import math

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)
        acc = 0
        odd_calculated = False
        for letter, num in s_dict.items():
            if num % 2 == 0:
                acc += num
            else:
                if odd_calculated:
                    temp = num - 1
                    acc += temp
                else:
                    acc += num
                    odd_calculated = True

        return acc

s = "abcccdd"
solution = Solution()
print(solution.longestPalindrome(s))

