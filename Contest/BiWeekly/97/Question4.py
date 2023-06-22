from typing import *


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 0 or grid[m - 1][n - 1] == 0:
            return False

        dp_grid = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]

        for i in range(m):
            dp_grid[i][0][0] = grid[i][0]

        for j in range(n):
            dp_grid[0][j][0] = grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                for k in range(2):
                    left = grid[i - 1][j]
                    up = grid[i][j - 1]

                    dp_grid[i][j][k] = 1 if left or up else 0








grid = [[1,1,1],[1,0,0],[1,1,1]]
solution = Solution()
