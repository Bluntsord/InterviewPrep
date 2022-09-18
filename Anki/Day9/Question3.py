from typing import *


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.rstrip()
        if len(s) == 0:
            return 