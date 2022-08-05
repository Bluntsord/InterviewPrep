class Solution(object):
    def climbStairs(self, n):
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1

        first, second, counter = 1, 1, 1
        while counter != n:
            temp = second
            second = first + second
            first = temp
            counter += 1
        return second


