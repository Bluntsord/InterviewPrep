from typing import *

class Solution(object):
    def climbStairs(self, n):
        arr = [1, 2]
        if n < 0:
            return -1
        elif n <= 2:
            return arr[n - 1]

        for i in range(n - 2):
            temp = arr[0] + arr[1]
            arr[0] = arr[1]
            arr[1] = temp

        return temp

n = 6
solution = Solution()
print(solution.climbStairs(n))