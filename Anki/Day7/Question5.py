from typing import *
import queue as q

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.fresh_oranges_count = 0
        self.rotten_oranges = q.Queue()

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.fresh_oranges_count += 1
                elif grid[i][j] == 2:
                    self.rotten_oranges.put((i, j))

        visited = {}
        answer = 0
        while not self.rotten_oranges.empty():
            for i in range(self.rotten_oranges.qsize()):
                curr_node = self.rotten_oranges.get()
                if grid[curr_node[0]][curr_node[1]] == 1:
                    self.fresh_oranges_count -= 1
                neighbours = self.get_neighbours(curr_node)

                for neighbour in neighbours:
                    if neighbour not in visited and grid[neighbours[0]][neighbour[1]] == 1:
                        visited[neighbour] = 1
                        self.rotten_oranges.put(neighbour)
            answer += 1
        return answer if self.fresh_oranges_count == 0 else -1



    def get_neighbours(self, coord):
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid, answer))
        return answer


    def is_valid(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True
