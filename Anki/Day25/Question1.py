from typing import *

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        first, second = 1, 2
        for i in range(2, n):
            first, second = second, first + second

        return second

solution = Solution()
print(solution.climbStairs(4))
