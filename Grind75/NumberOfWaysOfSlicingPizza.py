from typing import *
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len((pizza[0]))
        prefix_grid = [[0 for _ in range(n)] for _ in range(m)]
        prefix_grid[m - 1][n - 1] = 1 if pizza[m - 1][n - 1] == "A" else 0

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                down = prefix_grid[i + 1][j] if i < m - 1 else 0
                right = prefix_grid[i][j + 1] if j < n - 1 else 0
                diag = prefix_grid[i + 1][j + 1] if i < m - 1 and j < n - 1 else 0
                curr = 1 if pizza[i][j] == "A" else 0
                prefix_grid[i][j] = down + right + curr - diag

        @lru_cache(None)
        def dp(row, col, number_of_cuts, prev_slice):
            if number_of_cuts == 1:
                return 1

            answer = 0
            for i in range(row + 1, m):
                if 0 < prefix_grid[i][col] < prev_slice:
                    answer += dp(i, col, number_of_cuts - 1, prefix_grid[i][col])

            for j in range(col + 1, n):
                if 0 < prefix_grid[row][j] < prev_slice:
                    answer += dp(row, j, number_of_cuts - 1, prefix_grid[row][j])

            mod = 10 ** 9 + 7
            return answer % mod

        return dp(0, 0, k, prefix_grid[0][0])

solution = Solution()
pizza = ["A..","AA.","..."]
k = 3
print(solution.ways(pizza, k))