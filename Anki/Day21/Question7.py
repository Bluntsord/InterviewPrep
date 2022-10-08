from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.m, self.n = len(matrix), len(matrix[0])
        self.visited = set()
        self.visited.add((0, 0))
        self.pointer = 0
        stack = [(0, 0)]

        answer = []
        while len(stack) != 0:
            curr_node = stack.pop()
            curr_val = matrix[curr_node[0]][curr_node[1]]
            print(curr_val)
            answer.append(curr_val)
            next_node = self.get_next_node(curr_node)
            if next_node is not None:
                self.visited.add(next_node)
                stack.append(next_node)

        return answer


    def get_next_node(self, curr_coord):
        next_direction = self.directions[self.pointer]
        next_coord = (curr_coord[0] + next_direction[0], curr_coord[1] + next_direction[1])
        if self.is_valid_coord(next_coord) and next_coord not in self.visited:
            return next_coord

        for i in range(4):
            self.pointer = (self.pointer + 1) % 4
            next_direction = self.directions[self.pointer]
            next_coord = (curr_coord[0] + next_direction[0], curr_coord[1] + next_direction[1])
            if self.is_valid_coord(next_coord) and next_coord not in self.visited:
                return next_coord

        return None

    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
print(solution.spiralOrder(matrix))