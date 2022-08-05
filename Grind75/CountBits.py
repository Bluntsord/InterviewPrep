class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)
        most_sig = 1

        for i in range(1, n + 1):
            if most_sig * 2 == i:
                most_sig = i
            dp[i] = 1 + dp[i - most_sig]

        return dp


n = 8
solution = Solution()
print(solution.countBits(n))