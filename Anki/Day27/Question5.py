from typing import *
import queue as q

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.k = k
        self.grid = grid
        self.directions = [(0, 1), (1, 0), (0, -1), (-1 , 0)]
        queue = q.Queue()
        visited = {}
        level = 0

        queue.put((0, 0, 0))

        while not queue.empty():
            for i in range(queue.qsize()):
                curr_coord = queue.get()
                if curr_coord[0] == self.m - 1 and curr_coord[1] == self.n - 1:
                    return level
                total_neighbours = self.get_neighbours(curr_coord, True)
                next_level_neighbours = [] if curr_coord[2] >= k else self.get_neighbours(curr_coord, False)
                total_neighbours.extend(next_level_neighbours)

                for neighbour in total_neighbours:
                    if neighbour in visited:
                        continue
                    visited[neighbour] = level
                    queue.put(neighbour)
            level += 1

        return -1

    def get_neighbours(self, coord, is_same_level):
        if is_same_level:
            answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1], coord[2]), self.directions)
            answer = filter(self.is_valid_square, answer)
            answer = filter(self.is_wall, answer)
            return list(answer)

        answer = map(lambda x: (x[0] + coord[0], x[1] + coord[1], coord[2] + 1), self.directions)
        answer = filter(self.is_valid_square, answer)
        return list(answer)

    def is_valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n or coord[2] < 0:
            return False
        return True

    def is_wall(self, coord):
        if self.grid[coord[0]][coord[1]] == 1:
            return False
        return True

solution = Solution()
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
print(solution.shortestPath(grid, 1))