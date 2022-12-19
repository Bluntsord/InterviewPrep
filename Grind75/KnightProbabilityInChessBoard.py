from typing import *


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.n = n
        dp_grid = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        start_coord = (row, column)
        self.directions = [(2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)]
        dp_grid[start_coord[0]][start_coord[1]][0] = 1


        for z in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    curr_coord = (i, j)
                    neighbours = self.get_neighbours(curr_coord)

                    for neighbour in neighbours:
                        dp_grid[i][j][z] += dp_grid[neighbour[0]][neighbour[1]][z - 1]/8

        answer = 0
        for i in range(n):
            for j in range(n):
                answer += dp_grid[i][j][k]

        return answer

    def get_neighbours(self, coord):
        answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1]), self.directions)
        answer = filter(self.is_valid, answer)

        return list(answer)


    def is_valid(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.n or coord[1] >= self.n:
            return False
        return True

solution = Solution()
n = 3
k = 2
row = 0
column = 0
print(solution.knightProbability(n, k, row, column))