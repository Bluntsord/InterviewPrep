class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_grid = [[1 for _ in range(n)] for _ in range(m)]
        print(dp_grid)
        for i in range(1, m):
            for j in range(1, n):
                dp_grid[i][j] = dp_grid[i - 1][j] + dp_grid[i][j - 1]

        return dp_grid[m - 1][n - 1]
