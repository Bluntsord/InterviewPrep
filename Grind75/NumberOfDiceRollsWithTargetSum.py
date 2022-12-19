from typing import *
from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @lru_cache(None)
        def dp(dices_left, target_left):
            if target_left // k > dices_left or dices_left == 0:
                return 0
            elif dices_left == 1:
                return 1 if 0 < target_left <= k else 0

            answer = 0
            for i in range(1, k + 1):
                answer += dp(dices_left - 1, target_left - i)

            return answer

        return dp(n, target)

solution = Solution()
n = 3
k = 6
target = 7
print(solution.numRollsToTarget(n, k, target))
