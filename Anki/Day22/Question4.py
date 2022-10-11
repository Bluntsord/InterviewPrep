from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp_grid = [[0 for _ in range(n)] for _ in range(m)]
        print(dp_grid)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp_grid[i][j] = 0
                elif i > 0 and j > 0:
                    dp_grid[i][j] = dp_grid[i - 1][j] + dp_grid[i][j - 1]
                elif i == 0 and j == 0:
                    dp_grid[i][j] = 1
                elif i == 0:
                    dp_grid[i][j] = dp_grid[i][j - 1]
                else:
                    dp_grid[i][j] = dp_grid[i - 1][j]
        return dp_grid[m - 1][n - 1] if obstacleGrid[0][0] != 1 else 0

solution = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(solution.uniquePathsWithObstacles(obstacleGrid))