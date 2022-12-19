from typing import *
from functools import lru_cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dp(pointer, steps_left):
            if pointer < 0 or pointer >= arrLen:
                return 0
            elif steps_left == 0:
                return 1 if pointer == 0 else 0

            move_right = dp(pointer + 1, steps_left - 1)
            move_left = dp(pointer - 1, steps_left - 1)
            stay_curr = dp(pointer, steps_left - 1)

            answer = move_left + move_right + stay_curr

            return answer

        return dp(0, steps)


solution = Solution()
steps = 2
arrLen = 4
print(solution.numWays(steps, arrLen))