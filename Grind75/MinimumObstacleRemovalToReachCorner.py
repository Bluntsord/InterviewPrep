from typing import *
import queue as q

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = q.PriorityQueue()
        queue.put((0, 0, 0, 0))
        visited = set()
        visited.add((0, 0))

        while not queue.empty() != 0:
            curr_coord = queue.get()
            if curr_coord[2] == self.m - 1 and curr_coord[3] == self.n - 1:
                return curr_coord[0]

            neighbours = self.get_neighbours(curr_coord, True)
            next_level_neighbours = self.get_neighbours(curr_coord, False)
            neighbours.extend(next_level_neighbours)

            for neighbour in neighbours:
                neighbour_without_level = (neighbour[2], neighbour[3])
                if neighbour_without_level in visited:
                    continue
                visited.add(neighbour_without_level)
                queue.put(neighbour)

        return -1

    def helper(self, coord):
        if self.is_valid_square(coord) and self.is_not_wall(coord):
            return True
        return False

    def get_neighbours(self, coord, is_same_level):
        if is_same_level:
            answer = map(lambda x: (coord[0], -1 * (coord[2] + coord[3] + x[0] + x[1]), coord[2] + x[0], coord[3] + x[1]), self.directions)
            answer = filter(self.is_valid_square, answer)
            answer = filter(self.is_not_wall, answer)
            
            return list(answer)

        answer = map(lambda x: (coord[0] + 1, -1 * (coord[2] + coord[3] + x[0] + x[1]), coord[2] + x[0], coord[3] + x[1]), self.directions)
        answer = filter(self.is_valid_square, answer)

        return list(answer)

    def is_not_wall(self, coord):
        if self.grid[coord[2]][coord[3]] == 1:
            return False
        return True

    def is_valid_square(self, coord):
        if coord[2] < 0 or coord[3] < 0 or coord[1] >= self.m or coord[2] >= self.n:
            return False
        return True

solution = Solution()
grid = [[0,1,1],[1,1,0],[1,1,0]]
print(solution.minimumObstacles(grid))