from typing import *
from queue import PriorityQueue

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.directions = [(0, 1), (1, 0)]
        pq = PriorityQueue()
        pq.put((grid[0][0], (0, 0)))
        visited = {}
        curr_stack = set()
        curr_stack.add((0, 0))
        visited[(0, 0)] = grid[0][0]

        while not pq.empty():
            weight, curr_coord = pq.get()
            curr_stack.remove(curr_coord)
            if curr_coord == (self.m - 1, self.n - 1):
                return weight
            neighbours = self.get_neighbours(curr_coord)

            for neighbour in neighbours:
                neighbour_weight = weight + grid[neighbour[0]][neighbour[1]]
                if neighbour in visited or neighbour in curr_stack:
                    continue
                visited[neighbour] = neighbour_weight
                curr_stack.add(neighbour)
                packaged = (neighbour_weight, neighbour)
                pq.put(packaged)

        return -1


    def get_neighbours(self, curr_coord):
        answer = list(map(lambda x: (x[0] + curr_coord[0], x[1] + curr_coord[1]), self.directions))
        answer = list(filter(self.is_valid_coord, answer))
        return answer


    def is_valid_coord(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
print(solution.minPathSum(grid))