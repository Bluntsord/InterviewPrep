from typing import *


class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.memo = {}
        self.x = x

        return self.helper(n)
    
    def helper(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return self.x
        elif n in self.memo:
            return self.memo[n]

        cut_off = n // 2
        first_half = self.helper(cut_off)
        second_half = self.helper(n - cut_off)
        answer = first_half * second_half
        self.memo[n] = answer

        return answer
