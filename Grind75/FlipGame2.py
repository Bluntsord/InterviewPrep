from typing import *
from functools import lru_cache

class Solution:
    def canWin(self, currentState):
        @lru_cache(None)
        def dfs(s):
            for i in range(1, len(s)):
                if s[i] == s[i - 1] == "+" and not dfs(s[:i - 1] + "--" + s[i + 1:]):
                    return True

            return False

        return dfs(currentState)

solution = Solution()
currState = "+++++"
print(solution.canWin(currState))







