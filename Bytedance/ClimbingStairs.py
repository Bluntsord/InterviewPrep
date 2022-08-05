class Solution(object):
    def climbStairs(self, n):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        elif n == 0:
            return 0

        take_one = 1 + Solution.climbStairs(n - 1)
        take_two = 1 + Solution.climbStairs(n - 2)
        return take_one + take_two



