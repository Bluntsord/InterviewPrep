from typing import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp_grid = [[-1 for _ in range(n)] for _ in range(m + 1)]

        for i in range(n):
            dp_grid[m][i] = i

        for i in reversed(range(m)):
            for j in range(n):
                if (j == 0 and grid[i][j] == -1) or (j == n - 1 and grid[i][j] == 1):
                    dp_grid[i][j] = -1
                    continue

                curr = grid[i][j]
                next = grid[i][j + 1] if curr == 1 else grid[i][j - 1]

                if curr != next:
                    dp_grid[i][j] = -1
                elif curr == 1:
                    dp_grid[i][j] = dp_grid[i + 1][j + 1]
                else:
                    dp_grid[i][j] = dp_grid[i + 1][j - 1]

        return dp_grid[0]

solution = Solution()
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
print(solution.findBall(grid))