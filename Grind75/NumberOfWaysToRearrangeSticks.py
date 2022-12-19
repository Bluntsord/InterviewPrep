import copy
import math
from typing import *
from functools import lru_cache

class Solution:

    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dp(n, k):
            if n == k:
                return 1
            elif k == 0:
                return 0

            first_case = dp(n - 1, k - 1)
            second_case = (n - 1) * dp(n - 1, k)

            return (first_case + second_case) % mod

        return dp(n, k)



solution = Solution()
n = 3
k = 2
print(solution.rearrangeSticks(n, k))


