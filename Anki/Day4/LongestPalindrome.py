import math
from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = dict(Counter(s))
        has_odd = False
        answer = 0
        for key, values in char_dict.items():
            if values % 2 == 1:
                has_odd = True

            values = math.floor(values/2) * 2
            answer += values

        return answer + 1 if has_odd else answer

