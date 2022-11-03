from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = matrix
        for i in range(self.m):
            curr_coord = (i, 0)
            if not self.is_diagonal_same(curr_coord):
                return False

        for j in range(self.n):
            curr_coord = (0, j)
            if not self.is_diagonal_same(curr_coord):
                return False

        return True

    def is_diagonal_same(self, coord):
        print("=======")
        curr = self.matrix[coord[0]][coord[1]]
        while self.is_valid_matrix(coord):
            if self.matrix[coord[0]][coord[1]] != curr:
                return False
            coord = (coord[0] + 1, coord[1] + 1)
            print(coord)
        return True

    def is_valid_matrix(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

solution = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(solution.isToeplitzMatrix(matrix))