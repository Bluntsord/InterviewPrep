from typing import *
from functools import lru_cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp_grid = [0 for _ in range(high + max(zero, one) + 1)]
        dp_grid[zero] += 1
        dp_grid[one] += 1
        mod = 10 ** 9 + 7

        for i in range(high + 1):
            dp_grid[i] %= mod
            dp_grid[i + zero] += dp_grid[i]
            dp_grid[i + one] += dp_grid[i]

        answer = 0
        for i in range(low, high + 1):
            answer += dp_grid[i]

        return answer % mod

solution = Solution()
low = 2
high = 3
zero = 1
one = 2
print(solution.countGoodStrings(low, high, zero, one))