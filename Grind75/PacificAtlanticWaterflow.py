import queue as q
from typing import *


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        pacific_shore = []
        atlantic_shore = []

        for i in range(self.m):
            for j in range(self.n):
                curr = (i, j)
                if i == 0 or j == 0:
                    pacific_shore.append(curr)

                if i == self.m - 1 or j == self.n - 1:
                    atlantic_shore.append(curr)

        pacific_rivers = self.dfs(pacific_shore)
        atlantic_rivers = self.dfs(atlantic_shore)

        answer = pacific_rivers.keys() & atlantic_rivers
        answer = list(answer)
        answer.sort(key=lambda x: x[0] * 10 + x[1])
        return answer

    def dfs(self, coord_list):
        visited = {}
        queue = q.Queue()
        for coord in coord_list:
            queue.put(coord)

        answer = {}

        while not queue.empty():
            curr_coord = queue.get()
            answer[curr_coord] = 1
            neighbours = self.get_valid_neighbours(curr_coord)

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited[neighbour] = 1
                    queue.put(neighbour)
        return answer


    def get_valid_neighbours(self, coord):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbours = map(lambda x: (x[0] + coord[0], x[1] + coord[1]), directions)
        temp = filter(self.is_valid, neighbours)
        valid_neighbours = list(filter(lambda x: self.can_water_flow(coord, x), temp))
        return valid_neighbours

    def is_valid(self, coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.m or coord[1] >= self.n:
            return False
        return True

    def can_water_flow(self, first_coord, second_coord):
        if self.heights[first_coord[0]][first_coord[1]] <= self.heights[second_coord[0]][second_coord[1]]:
            return True
        return False


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
solution = Solution()
answer = solution.pacificAtlantic(heights)
print(answer)