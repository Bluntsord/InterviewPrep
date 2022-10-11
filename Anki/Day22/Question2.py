from typing import *


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        if k == 0:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        self.k = k
        self.directions, self.grid = [(0, 1), (1, 0)], grid
        self.target = (self.m - 1, self.n - 1)
        self.answer = 0
        self.backTracking((0, 0), self.grid[0][0])

        return self.answer

    def backTracking(self, coord, acc):
        if not self.is_valid_coord(coord):
            return
        elif coord == self.target:
            self.answer += 1 if acc % self.k == 0 else 0
            return

        neighbours = self.get_neighbours(coord)
        for neighbour in neighbours:
            acc += self.grid[neighbour[0]][neighbour[1]]

            self.backTracking(neighbour, acc)

            acc -= self.grid[neighbour[0]][neighbour[1]]

    def get_neighbours(self, coord):
        answer = list(map(lambda x: (x[0] + coord[0], x[1] + coord[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True


grid = [[5,2,4],
        [3,0,5],
        [0,7,2]]

k = 3

solution = Solution()
print(solution.numberOfPaths(grid, k))