from typing import *
import queue as q

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        queue = q.Queue()
        visited = set()
        self.grid = grid
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                curr_value = grid[i][j]
                if curr_value == 2:
                    visited.add((i, j))
                    queue.put((i, j))
                elif curr_value == 1:
                    fresh_oranges += 1

        answer = 0
        while not queue.empty():
            for i in range(queue.qsize()):
                curr_coord = queue.get()
                neighbours = self.get_neighbours(curr_coord)

                for neighbour in neighbours:
                    if neighbour not in visited and self.grid[neighbour[0]][neighbour[1]] == 1:
                        visited.add(neighbour)
                        fresh_oranges -= 1
                        queue.put(neighbour)
            answer += 1

        return answer




    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def get_neighbours(self, coord):
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer

grid = [[2,1,1],[1,1,0],[0,1,1]]
solution = Solution()
print(solution.orangesRotting(grid))
