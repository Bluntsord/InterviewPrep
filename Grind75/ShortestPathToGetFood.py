from queue import Queue
from typing import *


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '*':
                    curr = (i, j)
                    break

        answer = self.bfs(curr)
        return answer

    def bfs(self, coord):
        queue = Queue()
        queue.put(coord)
        visited = {coord: 1}
        counter = 0
        while not queue.empty():
            for i in range(len(queue.queue)):
                curr_coord = queue.get()
                if self.is_goal(curr_coord):
                    return counter
                neighbours = self.get_neighbours(curr_coord)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited[neighbour] = 1
                        queue.put(neighbour)
            counter += 1

        return -1

    def get_neighbours(self, coord):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1]), directions)
        answer = list(filter(self.is_valid_square, answer))
        return answer

    def is_goal(self, coord):
        if self.grid[coord[0]][coord[1]] == "#":
            return True
        return False

    def is_valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        elif self.grid[coord[0]][coord[1]] == "X":
            return False
        return True

grid = [["X","X","X","X","X","X"],
        ["X","*","O","O","O","X"],
        ["X","O","O","#","O","X"],
        ["X","X","X","X","X","X"]]

grid2 = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]

grid3 = [["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"],
        ["X", "O", "O", "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"]]

solution = Solution()
print(solution.getFood(grid))
print(solution.getFood(grid2))
print(solution.getFood(grid3))
