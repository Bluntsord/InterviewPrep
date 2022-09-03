from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.memo = [[0 for j in range(self.n)] for i in range(self.m)]
        max_square = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == "1" and (i == 0 or j == 0):
                    self.memo[i][j] = 1
                elif self.matrix[i - 1][j - 1] == "1":
                    self.memo[i][j] = min(self.memo[i - 1][j - 1], self.memo[i - 1][j], self.memo[i][j - 1]) + 1
                    max_square = max(max_square, self.memo[i][j])

        return max_square * max_square




