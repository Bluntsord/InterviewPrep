from typing import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = {}
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.visited = {}

        for i in range(self.m):
            for j in range(self.n):
                curr_coord = (i, j)
                if curr_coord not in self.visited:
                    self.dfs(curr_coord, -1)

        max_coord = max(self.visited, key=self.visited.get)
        print(self.visited)
        return self.visited[max_coord]

    def dfs(self, coord, prev_value):
        if not self.is_valid_coord(coord) or self.matrix[coord[0]][coord[1]] <= prev_value:
            return 0
        elif coord in self.visited:
            return self.visited[coord]

        neighbours = self.get_valid_neighbours(coord)
        answer = 1
        for neighbour in neighbours:
            answer = max(answer, 1 + self.dfs(neighbour, self.matrix[coord[0]][coord[1]]))
        self.visited[coord] = max(answer, self.visited.get(coord, 1))
        return max(answer, self.visited.get(coord, 1))




    def get_valid_neighbours(self, coord):
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer


    def is_smaller(self, first_coord, second_coord):
        if self.matrix[first_coord[0]][first_coord[1]] < self.matrix[second_coord[0]][second_coord[1]]:
            return True
        return False

    def is_larger(self, first_coord, second_coord):
        if self.matrix[first_coord[0]][first_coord[1]] > self.matrix[second_coord[0]][second_coord[1]]:
            return True
        return False

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

matrix = [[3,4,5],
          [3,2,6],
          [1,2,3],
          [0,1,2]]
solution = Solution()
print(solution.longestIncreasingPath(matrix))