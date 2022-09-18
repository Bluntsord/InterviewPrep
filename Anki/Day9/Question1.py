from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.counter = 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        start = (0, 0)
        stack = [start]
        self.visited = {start: 0}
        answer = []
        while len(stack) != 0:
            curr_node = stack.pop()
            answer.append(matrix[curr_node[0]][curr_node[1]])

            if len(answer) == self.m * self.n:
                break
            next_coord = self.get_next_direction(curr_node)

            self.visited[next_coord] = self.counter
            stack.append(next_coord)

        return answer

    def get_next_direction(self, coord):
        next_coord = (coord[0] + self.directions[self.counter][0], coord[1] + self.directions[self.counter][1])
        while not self.is_valid_square(next_coord) or next_coord in self.visited:
            self.counter += 1
            self.counter = self.counter % 4
            direction = self.directions[self.counter]
            next_coord = (coord[0] + direction[0], coord[1] + direction[1])

        return next_coord



    def is_valid_square(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
print(solution.spiralOrder(matrix))