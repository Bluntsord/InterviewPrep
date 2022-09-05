from typing import *
import queue as q

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        food = q.Queue()
        self.m = len(grid)
        self.n = len(grid[0])
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "*":
                    end = (i, j)
                elif grid[i][j] == "#":
                    food.put((i, j))

        answer = 0
        visited = {}
        # print(end)
        while not food.empty():
            for i in range(food.qsize()):
                curr_coord = food.get()

                neighbours = self.get_neighbours(curr_coord)
                for neighbour in neighbours:
                    if neighbour == end:
                        return answer + 1

                    if neighbour not in visited and grid[neighbour[0]][neighbour[1]] != "X":
                        visited[neighbour] = 1
                        food.put(neighbour)

            answer += 1
        return -1

    def is_inside_grid(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def get_neighbours(self, coord):
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_inside_grid, answer))
        return answer

grid = [["X","X","X","X","X","X"],
        ["X","*","O","O","O","X"],
        ["X","O","O","#","O","X"],
        ["X","X","X","X","X","X"]]
solution = Solution()
print(solution.getFood(grid))