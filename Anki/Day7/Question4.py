import math
from typing import *


class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.memo = {}
        self.x = x

        return self.dp(n) if n >= 0 else 1/self.dp(n)

    def dp(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return self.x
        elif n in self.memo:
            return self.memo[n]

        first_half = int(math.floor(n/2))
        answer = self.dp(first_half) * self.dp(n - first_half)
        self.memo[n] = answer

        return answer