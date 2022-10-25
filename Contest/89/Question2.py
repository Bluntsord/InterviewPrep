import math
from typing import *


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = 10 ** 9 + 7
        while n > 0:
            curr = math.floor(math.log2(n))
            n -= 2 ** curr
            powers.append(curr)
        powers = list(map(lambda x: 2 ** x, reversed(powers)))
        acc = 1
        prefix_query = []
        print(powers)
        for curr in powers:
            acc *= curr
            prefix_query.append(acc)

        answer = []
        for first, second in queries:
            if first == 0 and second == 0:
                answer.append(prefix_query[0] % mod)
            elif first == 0:
                answer.append(prefix_query[second] % mod)
            else:
                first_operand = prefix_query[first - 1]
                second_operand = prefix_query[second]
                answer.append(int(second_operand/first_operand) % mod)
        return answer

solution = Solution()
n = 15
queries = [[0,1],[2,2],[0,3]]
print(solution.productQueries(n, queries))