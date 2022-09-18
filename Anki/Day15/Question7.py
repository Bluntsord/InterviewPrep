from typing import *
import queue as q

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = q.Queue()
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.m, self.n = len(mat), len(mat[0])
        visited = set()
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 0:
                    queue.put((i, j))
                    visited.add((i, j))

        answer = [[0 for j in range(self.n)] for i in range(self.m)]
        level = 0
        while not queue.empty():
            for i in range(queue.qsize()):
                curr_coord = queue.get()
                answer[curr_coord[0]][curr_coord[1]] = level

                neighbours = self.get_neighbours(curr_coord)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.put(neighbour)

        return answer


    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def get_neighbours(self, coord):
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer




