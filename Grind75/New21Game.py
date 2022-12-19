from typing import *
from functools import lru_cache
from collections import defaultdict

class Solution(object):
    def new21Game(self, N, K, max_value):
        if K == 0 or N >= K + max_value: return 1
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / max_value
            if i < K: Wsum += dp[i]
            if i - max_value >= 0: Wsum -= dp[i - max_value]
        return sum(dp[K:])


solution = Solution()
n = 21
k = 17
maxPts = 10
print(solution.new21Game(n, k, maxPts))





