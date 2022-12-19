from typing import *


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp_grid = [[0 for _ in range(n)] for _ in range(m)]
        answer = 0
        for i in range(m):
            if matrix[i][0] == 1:
                dp_grid[i][0] = 1
                answer += 1

        for j in range(1, n):
            if matrix[0][j] == 1:
                dp_grid[0][j] = 1
                answer += 1


        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue

                diag = dp_grid[i - 1][j - 1]
                left = dp_grid[i][j - 1]
                up = dp_grid[i - 1][j]

                dp_grid[i][j] = min(diag, left, up) + 1
                answer += dp_grid[i][j]

        for row in dp_grid:
            print(row)

        return answer

matrix = [
  [1, 0, 1],
  [1,1,0],
  [1,1,0]
]

solution = Solution()
print(solution.countSquares(matrix))
