import functools
from typing import *

forest = [[1, 2, 3],
          [2, 1, 2],
          [3, 1, 1]]

number = 3

class Solution:
    def ways(self, forest: List[str], k: int) -> int:
        self.m, self.n = len(forest), len(forest[0])
        self.memo = {}
        self.suffix_matrix = [[0 for j in range(self.n)] for i in range(self.m)]

        for i in reversed(range(self.m)):
            for j in reversed(range(self.n)):
                diag = self.suffix_matrix[i + 1][j + 1] if i != self.m - 1 and j != self.n - 1 else 0
                right = self.suffix_matrix[i][j + 1] if j != self.n - 1 else 0
                down = self.suffix_matrix[i + 1][j] if i != self.m - 1 else 0
                self.suffix_matrix[i][j] = right + down - diag
                self.suffix_matrix[i][j] += 1 if forest[i][j] == 2 else 0

        mod = 10 ** 9 + 7
        answer = self.backTracking(0, 0, k, self.suffix_matrix[0][0]) % mod

        return answer

    def backTracking(self, row, col, islands_left, count):
        key = (row, col, islands_left)
        if islands_left == 1:
            return 1
        elif key in self.memo:
            return self.memo[key]

        answer = 0
        for i in range(row + 1, self.m):
            if 0 < self.suffix_matrix[i][col] < count:
                answer += self.backTracking(i, col, islands_left - 1, self.suffix_matrix[i][col])

        for j in range(col + 1, self.n):
            if 0 < self.suffix_matrix[row][j] < count:
                answer += self.backTracking(row, j, islands_left - 1, self.suffix_matrix[row][j])

        self.memo[key] = answer
        return answer

solution = Solution()
print(solution.ways(forest, number))