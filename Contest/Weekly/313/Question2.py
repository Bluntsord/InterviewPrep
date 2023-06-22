from typing import *


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.sum_left_prefix_matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            acc = 0
            for j in range(n):
                acc += grid[i][j]
                self.sum_left_prefix_matrix[i][j] = acc

        answer = 0
        for i in range(m - 2):
            for j in range(n - 2):
                answer = max(answer, self.get_hour_glass(i, j))

        return answer



    def get_hour_glass(self, m, n):
        sum_first_row = self.sum_left_prefix_matrix[m][n + 2]
        sum_first_row -= self.sum_left_prefix_matrix[m][n - 1] if n != 0 else 0

        sum_last_row = self.sum_left_prefix_matrix[m + 2][n + 2]
        sum_last_row -= self.sum_left_prefix_matrix[m + 2][n - 1] if n != 0 else 0

        return sum_first_row + sum_last_row + self.grid[m + 1][n + 1]

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
solution = Solution()
print(solution.maxSum(grid))

