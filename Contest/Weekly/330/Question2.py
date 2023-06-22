from typing import *


class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ways = pow(2, n, mod) - 2
        return ways % mod

solution = Solution()
print(solution.monkeyMove(10))