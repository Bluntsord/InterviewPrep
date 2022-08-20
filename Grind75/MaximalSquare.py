from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        self.memo = {}
        self.m = len(matrix)
        self.n = len(matrix[0])
        base_coord = (0, 0)
        self.answer = 0
        self.dp(base_coord)
        test = (0, 1)

        return self.answer ** 2

    def dp(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return 0
        elif coord in self.memo:
            return self.memo[coord]

        curr = self.matrix[coord[0]][coord[1]]
        down = (coord[0] + 1, coord[1])
        right = (coord[0], coord[1] + 1)
        diag = (coord[0] + 1, coord[1] + 1)

        down_wish = self.dp(down)
        right_wish = self.dp(right)
        diag_wish = self.dp(diag)
        if curr == 0 or curr == '0':
            answer = 0
        else:
            answer = 1 + min(down_wish, right_wish, diag_wish)

        self.memo[coord] = answer
        self.answer = max(self.answer, answer)
        return answer

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["0","1"],["1","0"]]
solution = Solution()
print(solution.maximalSquare(matrix))