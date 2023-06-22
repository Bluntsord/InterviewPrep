from typing import *


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if i == j or i + j == self.n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True


grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
solution = Solution()
print(solution.checkXMatrix(grid))