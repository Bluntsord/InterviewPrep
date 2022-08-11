from typing import *


class Solution:
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        print(index)
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:  # A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD


solution = Solution()
arr = [2, 4, 5, 10]
print(solution.numFactoredBinaryTrees(arr))








