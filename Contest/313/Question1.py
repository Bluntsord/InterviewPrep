import math
from typing import *


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        first = a if a > b else b
        second = b if a > b else a
        answer = 0
        for i in range(1, second + 1):
            if second % i == 0 and first % i == 0:
                answer += 1
        return answer


a = 12
b = 6
solution = Solution()
print(solution.commonFactors(a, b))
