from typing import *

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        answer, acc = 0, 0
        for i in range(1, n + 1):
            if i in banned_set:
                continue
            elif acc + i > maxSum:
                return answer
            answer += 1
            acc += i

        return answer

solution = Solution()
banned = [1,6,5]
n = 5
maxSum = 1
print(solution.maxCount(banned, n, maxSum))