from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        print(memo)
        answer = 0
        for i in range(1, m):
            for j in range(1, n):
                if memo[i][j] == 1:
                    answer = max(answer, 1)
                curr = min(memo[i - 1][j - 1], memo[i][j - 1], memo[i - 1][j]) + 1 if memo[i][j] == 1 else 0
                answer = max(answer, curr)

        return answer ** 2
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

solution = Solution()
print(solution.maximalSquare(matrix))