from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.visited = {}
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.direction = 0
        self.answer = []
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.traverse((0, 0))
        self.answer_matrix = [[-1 for _ in self.m] for _ in self.n]
        print(self.answer_matrix)

        return self.answer

    def traverse(self, coord):
        curr = coord

        while curr is not None:
            value = self.matrix[curr[0]][curr[1]]
            self.answer.append(value)
            self.visited[curr] = 1
            curr = self.get_next_direction(curr)


    def is_inside_board(self, coord):
        if coord[0] >= 0 and coord[1] >= 0 and coord[0] < self.m and coord[1] < self.n:
            return True
        return False

    def get_next_direction(self, coord):
        for i in range(4):
            self.direction = self.direction % 4
            direction = self.directions[self.direction]
            next = (coord[0] + direction[0], coord[1] + direction[1])
            if self.is_inside_board(next) and next not in self.visited:
                return next
            self.direction += 1

        return None

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
print(solution.spiralOrder(matrix2))