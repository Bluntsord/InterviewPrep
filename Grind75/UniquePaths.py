class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo_grid = [[-1] * n for _ in range(m)]

        for i in range(n):
            self.memo_grid[0][i] = 1

        for i in range(m):
            self.memo_grid[i][0] = 1

        for i in range(m):
            for j in range(n):
                curr = self.memo_grid[i][j]
                if curr == -1:
                    self.memo_grid[i][j] = self.memo_grid[i - 1][j] + self.memo_grid[i][j - 1]

        return self.memo_grid[m - 1][n - 1]

solution = Solution()
print(solution.uniquePaths(3, 5))
