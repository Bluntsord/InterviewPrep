import math
from typing import *


class Solution:
    def monkeyMove(self, n: int) -> int:
        if n % 2 == 0:
            first, second = int(n / 2), int(n / 2)
        else:
            first, second = n // 2, (n // 2) + 1

        first_round = (2 ** first) - 2
        second_round = (2 ** second) - 2

        answer = 2 ** n - (first_round + second_round)
        return answer

solution = Solution()
print(solution.monkeyMove(10))
