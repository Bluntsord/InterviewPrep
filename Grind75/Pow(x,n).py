import math
from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.memo = {}
        if n < 0:
            return 1/self.dp(x, -n)
        return self.dp(x, n)

    def dp(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n in self.memo:
            return self.memo[n]

        first_half = math.floor(n/2)
        second_half = n - first_half
        first_wish = self.dp(x, first_half)
        second_wish = self.dp(x, second_half)
        answer = first_wish * second_wish
        self.memo[n] = answer

        return answer

solution = Solution()
print(solution.myPow(2, -5))
