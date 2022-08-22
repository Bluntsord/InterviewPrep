from typing import *

class Solution:
    def solution(self, n, k):
        self.memo = {}
        self.n = n
        self.k = k
        answer = 0
        glasses = {i: 1 for i in reversed(range(n))}
        # print(glasses.keys())
        for glass in glasses.keys():
            self.k -= glass
            answer += 1
            if self.k < 0 and glass != 1:
                answer -= 1
                break
        return answer

n1 = 5
k1 = 8

n2 = 10
k2 = 5

solution = Solution()
print(solution.solution(n1, k1))
print(solution.solution(n2, k2))


