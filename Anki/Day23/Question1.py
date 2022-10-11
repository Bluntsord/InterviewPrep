from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp_grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp_grid[i][j] = grid[i][j]
                if i == 0 and j == 0:
                    continue
                up = dp_grid[i - 1][j] if i > 0 else float('inf')
                left = dp_grid[i][j - 1] if j > 0 else float('inf')
                dp_grid[i][j] += min(up, left)

        for row in dp_grid:
            print(row)
        return dp_grid[m - 1][n - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
print(solution.minPathSum(grid))
